#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import yaml
import argparse
import logging
import importlib
import tempfile
import logging.config
import collections
import magic


from . import __meta__
from . import  out
from . import engines


_LOG = logging.getLogger(__name__)

_MODE_SIMPLE  = 1
_MODE_COMPLEX = 2

_SETTINGS = None


class VideoTitle(object):

    def __init__(self, abs_path, mode, prefix, names):

        self._path   = abs_path
        self._mode   = mode
        self._prefix = prefix
        self._names  = names


    def __str__(self):

        if self._mode == 1:
            m = 'simple'
        else:
            m = 'complex'

        return "path:%s mode:%s prefix:%s names:%s" % (
            self._path,
            m,
            self._prefix,
            self._names
        )

    def __repr__(self):

        return self.__str__()


    def paths(self):

        p = list()
        if self._mode == _MODE_SIMPLE:
            for n in self._names:
                p.append(os.path.join(self._path, n))
        else:
            p.append(self._path)

        return p


    def files(self):

        return self._names


    def mode(self):

        return self._mode


    def prefix(self):

        return self._prefix


class VideoFile(object):

    def __init__(self, filename, path, mode, prefix, rawfile=None):

        if prefix.lower() != 'none':
            self.filename = "%s.%s" % (filename, prefix)
        else:
            self.filename = filename
        self.path     = path
        self.mode     = mode

        if self.mode == _MODE_COMPLEX:
            pattern, res = _extract_pattern(rawfile)
            if pattern is not None:

                if len(res) == 3:
                    self.season, self.episode = int(res[0]), int(res[1])
                else:
                    self.season, self.episode = None, int(res[0])

                self.pattern = pattern


    def __str__(self):

        if not hasattr(self, 'season'):
            return self.filename
        else:
            if self.season is not None:
                return "%s S%02dE%02d" % (self.filename, self.season, self.episode)
            else:
                return "%s %02d" % (self.filename, self.episode)


    def __repr__(self):

        return self.__str__()


    def name(self):

        return self.__str__()


    def next(self, season=False):

        assert self.mode != _MODE_SIMPLE, "Can't call next (check your file)"
        if season == True:
            assert self.season is not None, "Incorrect parameters check self.season"

        if season and self.season is not None:
            self.season += 1
            self.episode = 1
        else:
            self.episode += 1


def _loop_directories(items):

    for dirinfo in items:
        for name, details in dirinfo.iteritems():
            yield (details.get('path'), details.get('mode'), details.get('prefix'))


def _extract_pattern(filename):

    for p in _SETTINGS['patterns']:
        m = p.search(filename)
        if not m: continue

        res = m.groups()
        return (p, res)

    return (None, None)


def _cast_vfiles(video_title):

    _LOG.debug("cast:%s" % video_title)
    _vfiles = list()

    if video_title.mode() == _MODE_SIMPLE:
        for p in video_title.paths():
            filename = os.path.basename(p)
            _vfiles.append(VideoFile(filename, p, video_title.mode(), video_title.prefix()))
    elif video_title.mode() == _MODE_COMPLEX:
        path     = video_title.paths().pop()
        filename = os.path.basename(path)
        for f in video_title.files():
            vf = VideoFile(filename, path, video_title.mode(), video_title.prefix(), f)
            if hasattr(vf, 'season'): _vfiles.append(vf)

        if not len(video_title.files()):
            p = os.path.basename(path)
            _vfiles.append(VideoFile(p, path, video_title.mode(), video_title.prefix(), "%s s01e00" % p))

    _LOG.debug("add:%r" % _vfiles)

    return _vfiles


def _loop_files(video_title):

    _vfiles = _cast_vfiles(video_title)

    if video_title.mode() == _MODE_SIMPLE:
        for vf in _vfiles: yield vf
    elif video_title.mode() == _MODE_COMPLEX:
        selected = 0
        s, e     = 0, 0
        for idx, vf in enumerate(_vfiles):
            if vf.season > s:
                s, e = vf.season, vf.episode
                selected = idx
            elif vf.season == s:
                if vf.episode > e:
                    s, e = vf.season, vf.episode
                    selected = idx
            elif vf.season is None:
                if vf.episode > e:
                    e = vf.episode
                    selected = idx

        if selected: yield _vfiles[selected]


def _extract_complex_content(path):

    mime = magic.Magic(mime=True)

    names = list()
    for root, dirs, files in os.walk(path):

        for f in files:
            p = os.path.join(root, f)
            if mime.from_file(p).split('/')[0] == 'video':
                names.append(f)

    return names


def check_results(filename, video_file):

    tocheck = video_file.name().replace('.', ' ').split(' ')

    for tc in tocheck:
        if tc.lower() not in filename.lower(): return False

    if video_file.mode == _MODE_COMPLEX:

        r = video_file.pattern.search(filename)
        if r is None: return False

        match = r.groups()
        if len(match) == 3:
            s, e = int(match[0]), int(match[1])
        else:
            s, e = None, int(match[0])

        return s == video_file.season and e == video_file.episode

    return True


def _output_resfile(engname, seed, filename):

    print "{0:20} {1} {2:3} {3} {4}".format("[%s]" %
                                            engname,
                                            'Seed:',
                                            seed,
                                            'File:',
                                            filename)

def _check_results_fmt(results):

    field = ['url', 'filename', 'seed']

    for res in results:
        for k in res.iterkeys():
            if k not in field: return False

            for f in field:
                if res.get(f, None) == None: return False

            if type(res['seed']) is not int: return False

    return True


def outfile(todownload):

    print "\tDownload -> ",
    _output_resfile(todownload.engine.name(),
                    todownload.results['seed'],
                    todownload.results['filename'])

    choice = _SETTINGS['out']['choice']
    call   = getattr(out, choice)

    call(todownload, _SETTINGS['out'][choice])


def download(video_file, torengines, recursion=True):

    _LOG.debug("process:%s" % video_file)
    print "\t[+] %s" % video_file

    fields     = ['engine', 'session', 'results', 'seed', 'vf']
    todownload = collections.namedtuple('Todownload', fields)

    todownload.seed = -1
    curseed         = -1

    for e in filter(lambda engine: engine not in _SETTINGS['excludes'], torengines):
        ret = e.get(video_file.name(), _SETTINGS['engines'][e.name()])
        if type(ret) is not tuple:
            _LOG.error("%s:ko return:%s need:tuple" % (e.name(), type(ret)))
            continue

        res, session = ret
        if not len(res): continue
        if not _check_results_fmt(res):
            TypeError("Bad results format for [ %s ]" % e.name())

        selected = -1
        for idx, r in enumerate(res):
            r['filename'] = r['filename'].encode('utf-8')

            if check_results(r['filename'], video_file) == True:
                _output_resfile(e.name(), r['seed'], r['filename'])
                if r['seed'] > curseed: curseed, selected = r['seed'], idx
            else:
                _LOG.debug("match:ko f1:%s f2:%s" % (r['filename'], video_file))

        if curseed > todownload.seed:
            todownload.engine  = e
            todownload.session = session
            todownload.results = res[selected]
            todownload.seed    = curseed
            todownload.vf      = video_file

    if curseed != -1:
        outfile(todownload)
        if video_file.mode == _MODE_COMPLEX:
            video_file.next()
            download(video_file, torengines)
    elif video_file.mode == _MODE_COMPLEX and video_file.season is not None and recursion:
        video_file.next(season = True)
        download(video_file, torengines, False)


def start(config, debug):

    global _SETTINGS

    if debug: print "[*] Debug mode activated"

    try:
        with open(config, 'r') as input:
            settings = yaml.safe_load(input)
            patterns = list()
            for p in settings['patterns']: patterns.append(re.compile(p))
            _SETTINGS = settings
            _SETTINGS['patterns'] = patterns
            if not debug:
                logging.disable(logging.CRITICAL)
            else:
                logging.config.dictConfig(_SETTINGS['logging'])
    except IOError as e:
        print e.strerror, "[ %s ]" % config
        return 1
    except yaml.YAMLError, exc:
        print "Error in configuration file:", str(exc).replace('\n', ' ')
        return 2

    torengines = []
    for e in engines.__all__:

        engine_pkg = importlib.import_module("downloader.engines.%s" % e)
        engine_cls = getattr(engine_pkg, e.capitalize())

        e_inst = engine_cls()
        if e_inst.name() not in _SETTINGS['excludes']:
            torengines.append( engine_cls() )


    for root_directory, mode, prefix in _loop_directories(_SETTINGS['paths']):
        _LOG.debug("enter:%s mode:%d prefix:%s" % (root_directory, mode, prefix))

        if mode == _MODE_SIMPLE:
            video_title = list()
            for item in os.listdir(root_directory):

                p = os.path.join(root_directory, item)
                if os.path.isdir(p):
                    if len(os.listdir(p)) == 0:
                        video_title.append(item)

            if len(video_title):
                vt = VideoTitle(root_directory, mode, prefix, video_title)
                for vf in _loop_files(vt):
                    download(vf, torengines)
        elif mode == _MODE_COMPLEX:
            for item in os.listdir(root_directory):
                video_title = list()

                p = os.path.join(root_directory, item)

                names = _extract_complex_content(p)
                video_title.extend(names)
                vt = VideoTitle(p, mode, prefix, video_title)
                for vf in _loop_files(vt):
                    vf.next()
                    download(vf, torengines)


def run():

    parser = argparse.ArgumentParser(
        version         = __meta__.__version__,
        description     = __meta__.__description__,
        epilog          = __meta__.__epilog__,
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('config',
                        action = 'store',
                        help   = 'configuration file')
    parser.add_argument('--debug',
                        action  = 'store_true',
                        default = False,
                        help    = 'debug mode [default:%(default)s]')

    opt = parser.parse_args()

    start(opt.config, opt.debug)
