#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import setuptools


execfile('downloader/__meta__.py')

NAME         = __project__
AUTHOR       = __author__
AUTHOR_EMAIL = __email__
VERSION      = __version__
DESCRIPTION  = __description__
MAINTAINER   = __maintainer__

BIN_PATH  = '/usr/bin' 
USR_PATH  = os.path.join('/usr/share', NAME)

libs = [
    'PyYaml',
    'requests',
    'cfscrape',
    'lxml'
]
install_requires = list()

if sys.version_info < (2, 7):
    install_requires.append('argparse')
install_requires.extend(libs)

files = list()
files.append( (BIN_PATH, ['bin/downloader']) )
files.append( (USR_PATH, ['config/downloader.cfg.example']) )

setuptools.setup (
    name                 = NAME,
    author               = AUTHOR,
    author_email         = AUTHOR_EMAIL,
    maintainer           = MAINTAINER,
    description          = DESCRIPTION,
    platforms            = ['GNU/Linux'],
    url                  = 'https://github.com/akil/downloader',
    version              = VERSION,
    packages             = ['downloader', 'downloader.engines'],
    scripts              = ['bin/downloader'],
    long_description     = open('README.md').read(),
    install_requires     = install_requires,
    include_package_data = True,
    data_files           = files,
    classifiers          = [
        "Development Status :: 4 - Beta",
        "Topic :: System :: Networking",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: GNU/Linux",
        "Environment :: Console",
    ]
)


print "\n************************************************"
print "Please check the default configuration file at:"
print "\t%s\n" % USR_PATH
print "$ mkdir -p ~/.config/downloader"
print "$ cp %s ~/.config/downloader\n" % os.path.join(USR_PATH, 'downloader.cfg.example')
print "*************************************************\n"

