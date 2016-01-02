# -*- coding: utf-8 -*-

import re
import os
import requests
import urllib2
import argparse
import tempfile
import importlib
import subprocess
import collections
import xml.dom.minidom

import downloader.engines

from __meta__ import __description__
from __meta__ import __version__


cmd_args      = ['transmission-remote', '10.42.13.4', '-a', '%s', '-c', '/opt/multimedia/incomplete', '-w',
                 '%s', '--pex', '--dht']
pattern_type2 = [
    re.compile(r"[\._ \-][Ss]([0-9]+)[\.\-]?[Ee]([0-9]+)([^\\/]*)"), # s01e02...
    re.compile(r"[\._ \-][Ee]?([0-9][0-9][0-9]?)([\._ \-][^\\/]*)"), # foo.102 ou foo.10 ou foo.E10
    re.compile(r"[\._ \-]([0-9]+)x([0-9]+)([^\\/]*)"),               # foo.1x09
    re.compile(r"^([0-9]{2,4})[\-_. ]"),                             # 01 - foo
    re.compile(r"\[[Ss]([0-9]+)\]_\[[Ee]([0-9]+)([^\\/]*)"),         # foo_[s01]_[e01]
    ]


class Config(object):
    def __init__(self, filename):
        self._file = filename
        self.dir   = list()

    def _get_data(self):
        xmldoc = xml.dom.minidom.parse(self._file)
        for item in xmldoc.getElementsByTagName('directory'):
            attr  = int(item.attributes['type'].value)
            value = "\n".join([x.data for x in item.childNodes])
            self.dir.append(
                collections.namedtuple('Dir', 'path type')._make([value, attr])
                )

    def read(self):
        self._get_data()

class Search(object):
    def __init__(self, filename, path, type, regex = None):
        self.name  = filename
        self.type  = type
        self.path  = path
        self.regex = regex

        self.s = None
        self.e = None

    def __repr__(self):
        s = ' '.join(filter(lambda x: x.isalnum(), re.split("(\W+)", self.name.lower())))
        if self.s is not None and self.e is not None:
            s += " S%02iE%02i" % (self.s, self.e)
        elif self.s is not None:
            s += " %02i" % self.s
        elif self.e is not None:
            s += " %02i" % self.e

        return s.replace(' ', '+')

    def __str__(self):
        return self.__repr__()


def load_class(full_class_string):
    class_data  = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str   = class_data[-1]

    module = importlib.import_module(module_path)

    return getattr(module, class_str)


def get_next_file(directory, path, stype):
    fdlist = os.listdir(directory)

    s, e, sprev, eprev, reg = (None, None, 0, 0, None)
    for filename in fdlist:
        for regex in pattern_type2:
            m = regex.search(filename)
            if not m: continue

            ret = m.groups()
            if len(ret) == 3:
                s, e = int(ret[0]), int(ret[1])
            else:
                s, e = None, int(ret[0])


            if s is not None:
                if sprev < s:
                    sprev = s
                    eprev = e
                elif eprev < e and sprev == s:
                    eprev = e
            elif eprev < e:
                eprev = e

            reg = regex

            break

    if not sprev and not eprev:
        return None

    search_file = Search(directory, path, stype, reg)
    if sprev: search_file.s = sprev
    if eprev: search_file.e = eprev

    return search_file

def is_right_file(filename, result_file):
    f1 = filename.name.lower()
    f2 = result_file.lower()

    retlst = f2.split('.')
    if len(retlst) <= 1:
        retlst = f2.split(' ')
        retlst = [ x.lower() for x in retlst ]
        
    if filename.type == 2:
        if filename.regex:
            m = filename.regex.search(f2)
            
            if not m:
                for p in pattern_type2:                    
                    m = p.search(f2)
                    if m: break
                if not m: return False            

            
            for f in f1.split('.'):
                if f.lower() not in retlst: return False
            
            ret = m.groups()
            if len(ret) == 3:
                s, e = int(ret[0]), int(ret[1])

                if filename.s == s and filename.e == e: return True
                return False
            else:
                if filename.e == int(ret[0]): return True
                return False
        else:
            for f in [f1, "s%02ie%02i" % (filename.s, filename.e)]:
                if f not in retlst: return False
            

    for fname in filter(lambda x: x.isalpha(), re.split("(\W+)", f1)):
        if f2.find(fname) == -1:
            return False

    return True

def get_it(torrent_url, prelink, path, session):

    if prelink is not None:
        if prelink.get('method') == 'post':
            session.post(prelink.get('url'), prelink.get('data'))
        else:
            session.get(prelink.get('url'))

    r        = session.get(torrent_url, stream=True)
    tmp_file = tempfile.NamedTemporaryFile().name + '.torrent'

    with open(tmp_file, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    r.close()

    cmd = (' '.join(cmd_args) % (tmp_file, path)).split()

    r = subprocess.Popen(cmd,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
    r.wait()

    os.remove(tmp_file)


def _download_file(fileobject, engines_list):
    
    print "\t* searching [ %s ]" % fileobject

    torrent, current_seed, engine_name = None, 0, None
    for e in engines_list:

        res, session = None, None

        try:
            res, session = e.get(fileobject)
        except requests.exceptions.ConnectionError:
            print '{0:20}{1}'.format("[%s]" % e.name(), "Unvailable")
            continue

        if res == None:
            print '{0:20}{1}'.format("[%s]" % e.name(), "Can't log-in")
            continue
        
        found = False
        for d in filter(lambda r : is_right_file(fileobject, r['filename']), res):
                
            print u"{0:20} {1} {2:3} {3} {4}".format("[%s]" %
                                                     e.name(),
                                                     'Seed:',
                                                     d['seed'],
                                                     'File:',
                                                     d['filename'])
            
            if int(d['seed']) > int(current_seed):
                current_seed, torrent, engine_name, engine_session = d['seed'], d, e.name(), session

            found = True

        if len(res) == 0:
            print '{0:20}{1}'.format("[%s]" % e.name(), "No result")

        if len(res) and found == False:
            print '{0:20}{1}'.format("[%s]" % e.name(), "No corresponding results")

    if torrent is not None:
        print "\t-> {0:18} Seed: {1:3} {2}".format("<%s>" % engine_name, torrent['seed'], torrent['filename'])
        get_it(torrent['url'], torrent.get('prelink', None), fileobject.path, engine_session)

        print ""

        return True

    print ""

    return False


def download(download_list, engines_list):
    
    for f in download_list:
        r = _download_file(f, engines_list)
        while r == True and f.type == 2:
            f.e = f.e + 1
            r = _download_file(f, engines_list)

        if r == False and f.type == 2:
            if f.s is not None:
                f.s, f.e = f.s + 1, 01
                r = _download_file(f, engines_list)


def main(config_file, exclude):
    
    cfg = Config(config_file)
    dwl = list()

    cfg.read()

    for d in cfg.dir:
        os.chdir(d.path)
        for f in filter(lambda f: not f.startswith('.') and os.path.isdir(f), os.listdir('.')):
            try:
                nfd = len(os.listdir(f))
            except OSError:
                continue

            if nfd == 0:
                if d.type == 1:
                    o = Search(f, os.path.join(d.path, f), d.type)
                    if o not in dwl: dwl.append(o)
                elif d.type == 2:
                    o = Search(f, os.path.join(d.path, f), d.type)
                    o.s, o.e = (1, 1)
                    if o not in dwl: dwl.append(o)
            elif d.type == 2:
                dlfile = get_next_file(f, os.path.join(d.path, f), d.type)

                if dlfile is not None:
                    if dlfile.e is None:
                        dlfile.e = 1
                    else:
                        dlfile.e += 1
                    if dlfile not in dwl: dwl.append(dlfile)


    engines_list = []
    for e in filter(lambda x: x not in exclude, downloader.engines.__all__):

        module     = __import__('downloader.engines')
        engine     = getattr(module, e)
        engine_cls = getattr(engine, e.capitalize())

        engines_list.append( engine_cls() )

    download(dwl, engines_list)


def run():
    parser = argparse.ArgumentParser(description     = __description__,
                                     version         = __version__,
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('config',
                        action  = 'store',
                        help    = 'configuration file')
    parser.add_argument('--exclude',
                        action  = 'store',
                        dest    = 'engine',
                        type    = str,
                        help    = 'exclude engine from search (--exclude=engine1,engine2)')


    opt = parser.parse_args()

    if opt.engine is None:
        exclude = []
    else:
        exclude = opt.engine.split(',')

    main(opt.config, exclude)
