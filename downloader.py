#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import urllib2
import argparse
import tempfile
import importlib
import subprocess
import collections
import xml.dom.minidom

import engines

cmd_args      = ['transmission-remote', 'localhost', '-a', '%s', '-c', '/mnt/external/Incomplete', '-w',
                 '%s', '--pex', '--dht']
pattern_type2 = [
    re.compile(r"[\._ \-][Ss]([0-9]+)[\.\-]?[Ee]([0-9]+)([^\\/]*)"), # s01e02...
    re.compile(r"[\._ \-]([0-9]+)x([0-9]+)([^\\/]*)"),               # foo.1x09
    re.compile(r"[\._ \-]E?([0-9][0-9][0-9]?)([\._ \-][^\\/]*)"),    # foo.102 ou foo.10 ou foo.E10
    re.compile(r"'^(?P<ep>[0-9]{1,3})[^0-9]'"),                      # 01 - foo
    re.compile(r"\[[Ss]([0-9]+)\]_\[[Ee]([0-9]+)([^\\/]*)"),         # foo_[s01]_[e01]
    ]

class Config(object):
    def __init__(self, filename):
        self._file = filename
        self.dir  = list()

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
    def __init__(self, filename, path, type):
        self.name = filename
        self.type = type
        self.path = path

        self.s = None
        self.e = None

    def __repr__(self):
        s = ' '.join(filter(lambda x: x.isalnum(), re.split("(\W+)", self.name.lower())))
        if self.s is not None: s += " %02i" % self.s
        if self.e is not None: s += " %02i" % self.e
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

    s, e, sprev, eprev = (None, None, 0, 0)
    for filename in fdlist:
        for regex in pattern_type2:
            m = regex.search(filename)
            if not m: continue

            ret = m.groups()
            if len(ret[1]) < 3:
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

            break

    if not sprev and not eprev:
        return None

    search_file = Search(directory, path, stype)
    if sprev: search_file.s = sprev
    if eprev: search_file.e = eprev

    return search_file

def is_right_file(filename, result_file):
    f1 = filename.name.lower()
    f2 = result_file.lower()

    if filename.type == 2:
        if filename.s:
            if f2.find("%02i" % filename.s) == -1:  return False
        if f2.find("%02i" % filename.e) == -1: return False

    for fname in filter(lambda x: x.isalpha(), re.split("(\W+)", f1)):
        if f2.find(fname) == -1:
            return False

    return True

def get_it(torrent_url, path, cookie):
    request  = urllib2.Request(torrent_url,
                               headers = {'cookie': cookie})
    contents = urllib2.urlopen(request).read()

    tmp_file = tempfile.NamedTemporaryFile().name
    fd = open(tmp_file, "wb")
    fd.write(contents)
    fd.close()

    cmd = (' '.join(cmd_args) % (tmp_file, path)).split()

    subprocess.Popen(cmd,
                     stdout = subprocess.PIPE,
                     stderr = subprocess.PIPE)

    os.remove(tmp_file)


def download(download_list, engines_list):
    for f in download_list:
        for e in engines_list:
            print "\t* searching [ %s ]" % f
            res, cookie = e.get(f)
            if not len(res):
                print "[%s] No result for %s" % (e.name(), f)
                continue

            torrent, current_seed = None, 0
            for d in filter(lambda r : is_right_file(f, r['filename']), res):
                print  "[{0}] Seed: {1:3} File: {2}".format(e.name(), d['seed'], d['filename'])
                if int(d['seed']) > int(current_seed): current_seed, torrent = d['seed'], d

            if torrent is None:
                print "[%s] No result for %s" % (e.name(), f)
                continue

            print "\t-> <{0}> Seed: {1:3} {2}\n".format(e.name(), torrent['seed'], torrent['filename'])
            get_it(torrent['url'], f.path, cookie)

def main(config_file):
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
                    dwl.append(Search(f, os.path.join(d.path, f), d.type))
                elif d.type == 2:
                    o   = Search(f, os.path.join(d.path, f), d.type)
                    o.e = 1
                    dwl.append(o)
            elif d.type == 2:
                dlfile = get_next_file(f, os.path.join(d.path, f), d.type)
                if dlfile is not None:
                    dlfile.e += 1
                    dwl.append(dlfile)

    engines_list = []
    for e in engines.__all__:
        cl = load_class("%s.%s.%s" % ('engines', e, e.capitalize()))
        engines_list.append(cl())

    download(dwl, engines_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description     = 'Download files from torrent engine.',
                                     formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    args = [
        [('-c', '--config'),
         {'type': str, 'default': 'downloader.cfg', 'help': 'configuration file'}]
        ]
    for name, arg in args:
        parser.add_argument(*name, **arg)

    opt = parser.parse_args()

    main(opt.config)
