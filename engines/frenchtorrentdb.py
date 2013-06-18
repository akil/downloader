#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HTMLParser
import urllib

from engine import Engine

#class ParseFrenchtorrentdb(sgmllib.SGMLParser):
#    def reset(self):
#        sgmllib.SGMLParser.reset(self)


class ParseSecureLogin(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self._secure_login = None

    def handle_starttag(self, tag, attrs):
        if tag != 'input': return

        in_secure_flag = False
        for k, v in attrs:
            if k == 'name' and v == 'secure_login':
                in_secure_flag = True
            elif k == 'value' and in_secure_flag:
                self._secure_login = v
                self.reset()

    def get_secure_flag(self):
        return self._secure_login

class Frenchtorrentdb(Engine):
    def __init__(self):
        self._name = 'frenchtorrentdb'
        self._url  = 'http://www.frenchtorrentdb.com'

    def name(self):
        return self._name

    def url(self):
        return self._url

    def get(self, filename):
        parser = ParseSecureLogin()
        page   = urllib.urlopen(self._url)

        parser.feed(page.read())
        page.close()
        parser.close()

        secure_flag = parser.get_secure_flag()
        
        #params = urllib.urlencode({'username': 'tototiti',
        #                           'password':'42klm256',
        #                           'secure_login': secure_flag})
        #page = urllib.urlopen(self._url + '/?section=LOGIN', params)
        
        
