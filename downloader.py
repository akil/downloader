#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import argparse
import xml.dom.minidom
import collections

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
    def __init__(self, filename, type):
        self.name = filename
        self.type = type

        self.s = None
        self.e = None

    def __repr__(self):
        s = self.name
        if self.s is not None: s += " %i" % self.s
        if self.e is not None: s += " %i" % self.e
        return s

    def __str__(self):
        return self.__repr__()


def get_next_file(directory, stype):
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

    search_file = Search(directory, stype)
    if sprev: search_file.s = sprev
    if eprev: search_file.e = eprev

    return search_file


def download(download_list):
    from engines.frenchtorrentdb import Frenchtorrentdb
    import sys
    e = Frenchtorrentdb()
    e.get("toto")
    sys.exit(42)
#    for f in download_list:
#        print f

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

            if nfd == 0 and d.type == 1:
                dwl.append(Search(f, d.type))
            elif nfd == 0:
                dwl.append(Search("%s %i" % (f, 01), d.type))
            elif d.type != 1:
                dlfile = get_next_file(f, d.type)
                if dlfile is not None:
                    dlfile.e += 1
                    dwl.append(dlfile)

    download(dwl)

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
