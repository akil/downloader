#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import setuptools

execfile('downloader/__meta__.py')

NAME         = __app_name__
AUTHOR       = __author__
AUTHOR_EMAIL = __email__
VERSION      = __version__
DESCRIPTION  = __description__
MAINTAINER   = __maintainer__
URL          = __url__

BIN_PATH  = '/usr/bin' 
CONF_PATH = os.path.join('/etc/', NAME)
USR_PATH  = os.path.join('/usr/share', NAME)

lib_tiers = [
    'lxml >= 3.4.2',
    'requests >= 2.2.1',
    'pyOpenSSL >= 0.13'
]
install_requires = list()

if sys.version_info < (2, 7):
    install_requires.append('argparse >= 1.1')
install_requires.extend(lib_tiers)

data_files = list()
data_files.append( (BIN_PATH, ['bin/downloader']) )
data_files.append( (CONF_PATH, ['config/downloader.example.cfg']) )
data_files.append( (os.path.join(USR_PATH, 'docs'),  glob.glob('docs/*')) )

setuptools.setup (
    name                 = NAME,
    author               = AUTHOR,
    author_email         = AUTHOR_EMAIL,
    maintainer           = MAINTAINER,
    description          = DESCRIPTION,
    platforms            = ['GNU/Linux'],
    url                  = URL,
    version              = VERSION,
    packages             = ['downloader', 'downloader.engines'],
    scripts              = ['bin/downloader'],
    long_description     = open('README').read(),
    install_requires     = install_requires,
    include_package_data = True,
    data_files           = data_files,
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
