#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sgmllib
import urllib2
import urllib
import urlparse

from engine import Engine

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
    regnme = re.compile(r"torrents_name\s{1}")
    reglnk = re.compile(r"torrents_download\s{1}")
    regsed = re.compile(r"torrents_seeders\s{1}")

    def reset(self):
        sgmllib.SGMLParser.reset(self)
        self._in_name = self._in_seed = self._in_dl = False
        self.results, self.tmp_results, self.pages_url = ([], {}, [])
        self.chk_page_num = []

    def start_li(self, attrs):
        for k, v in attrs:
            if k == 'class' and self.regnme.search(v):
                self._in_name = True
            elif k == 'class' and self.regsed.search(v):
                self._in_seed = True
            elif k == 'class' and self.reglnk.search(v):
                self._in_dl = True

    def start_a(self, attrs):
        for k, v in attrs:
            if k == 'href' and v.find('navname=#nav_') != -1:
                p = [ x for x in v.split('&') if x.find('page') != -1 ].pop().split('=')[1]
                if int(p) > 1 and not p in self.chk_page_num:
                    self.pages_url.append(v)
                    self.chk_page_num.append(p)
            elif k == 'class' and v == 'torrents_name_link':
                self._in_name = True
            elif not self._in_dl: continue
            elif k == 'href':
                self.tmp_results['url'] = v
                self.results.append(self.tmp_results)
                self.tmp_results = {}
                self._in_dl = False

    def handle_data(self, data):
        if self._in_name and len(data) > 1:
            self.tmp_results['filename'] = data.strip()
            self._in_name = False
        elif self._in_seed:
            self.tmp_results['seed'] = data
            self._in_seed = False

class Frenchtorrentdb(Engine):
    def __init__(self):
        self._name       = 'frenchtorrentdb'
        self._username   = 'tototiti'
        self._password   = '42klm256'
        self._url_login  = 'http://www.frenchtorrentdb.com/?section=LOGIN'
        self._url_search = 'http://www.frenchtorrentdb.com/?section=TORRENTS&exact=1&name=%s&submit=GO'
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

    def _get_page_content(self, url):
        request  = urllib2.Request(url.replace(' ', '.'),
                                   headers = {'cookie': self._cookie})
        contents = urllib2.urlopen(request).read()

        return contents

    def _get_results_from_page(self, url_page, parser):
        contents = self._get_page_content(url_page)
        parser.feed(contents)
        parser.close()
        return parser.results

    def _append_results(self, appending, results):
        for item in results:
            d = {}
            for k, v in item.iteritems():
                if k == 'url':
                    d['url'] = self.url() + v
                else:
                    d[k] = v
            appending.append(d)

    def _search(self, filename):
        results  = list()
        contents = self._get_page_content(self._url_search % filename)

        p = ParserSearch()
        p.feed(contents)
        p.close()

        self._append_results(results, p.results)

        pages_url = list(p.pages_url)
        for page_url in pages_url:
            items = self._get_results_from_page(self.url() + page_url, ParserSearch())
            self._append_results(results, items)

        return results, self._cookie

    def name(self):
        return self._name

    def url(self):
        return 'http://' + urlparse.urlparse(self._url_login).netloc

    def get(self, filename):
        if not self._cookie:
            secure_flag = self._get_secure_flag()
            self._login(secure_flag)

        return self._search(filename)
