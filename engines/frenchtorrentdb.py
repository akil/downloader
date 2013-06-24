#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sgmllib
import urllib2
import urllib
import urlparse

from engine import Engine

#class ParseFrenchtorrentdb(sgmllib.SGMLParser):
#    def reset(self):
#        sgmllib.SGMLParser.reset(self)


class ParseSecureLogin(sgmllib.SGMLParser):
    def reset(self):
        sgmllib.SGMLParser.reset(self)
        self._secure_login = None

    def start_input(self, attrs):        
        if not len(attrs): return
        in_secure_tag = False
        for k, v in attrs:
            if k == 'name' and v == 'secure_login':
                in_secure_tag = True
            elif k == 'value' and in_secure_tag:
                self._secure_login = v
                self.setnomoretags()
                break

    def get_secure_flag(self):
        return self._secure_login

class ParserSearch(sgmllib.SGMLParser):
    def reset(self):
        sgmllib.SGMLParser.reset(self)
        self._in_name = self._in_seed = self._in_dl = False

    def start_li(self, attrs):
        for k, v in attrs:
            if k == 'class' and v == 'torrents_name data_alt':
                self._in_name = True
            elif k == 'class' and v == 'torrents_seeders data_alt':
                self._in_seed = True
            elif k == 'class' and v == 'torrents_download data_alt':
                self._in_dl = True

    def start_a(self, attrs):
        if self._in_dl:
            v = [v for k, v in attrs if k == 'href']
            self._in_dl = False
            print 'Url  :' + v.pop()
            print "\n"

    def handle_data(self, data):
        if self._in_name:
            print 'File :' + data
        elif self._in_seed:
            print 'Seed :' + data


        self._in_name = self._in_seed = False

class Frenchtorrentdb(Engine):
    def __init__(self):
        self._name       = 'frenchtorrentdb'
        self._username   = 'tototiti'
        self._password   = '42klm256'
        self._url_login  = 'http://www.frenchtorrentdb.com/?section=LOGIN'
        self._url_search = 'http://www.frenchtorrentdb.com/?section=TORRENTS&name=%s&submit=Connexion'
        self._cookie     = None

    def _get_secure_flag(self):
        parser = ParseSecureLogin()
        page   = urllib2.urlopen(self._url_login)
        
        self._cookie = page.info()['set-cookie'].split(';', 1)[0]

        parser.feed(page.read())
        page.close()
        parser.close()

        return parser.get_secure_flag()
        
    def _login(self, secure_flag):
        params = urllib.urlencode({'username': self._username,
                                   'password': self._password,
                                   'secure_login': secure_flag,
                                   'submit': 'Connection'})
        req = urllib2.Request(self._url_login, params,
                              headers = {'cookie': self._cookie})
        res = urllib2.urlopen(req)

        cookie = res.info().get('set-cookie', None)
        if cookie: self._cookie = cookie.split(';', 1)[0]

        res.close()

    def _search(self, filename):
        request = urllib2.Request(self._url_search % filename,
                                  headers = {'cookie': self._cookie})
        contents = urllib2.urlopen(request).read()

        p = ParserSearch()
        p.feed(contents)
        p.close()

    def name(self):
        return self._name

    def url(self):
        return urlparse.urlparse(self._url_login).netloc

    def get(self, filename):
        proxy = urllib2.ProxyHandler({'http': '10.42.42.3:8080'})
        opener = urllib2.build_opener(proxy, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        if not self._cookie:
            secure_flag = self._get_secure_flag()
            self._login(secure_flag)

        self._search(filename)


        
        
        
