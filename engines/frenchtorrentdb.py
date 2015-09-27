#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sgmllib
import urllib2
import urllib
import urlparse
import PyV8

from engine import Engine

url_cookie    = 'http://www.frenchtorrentdb.com/?section=LOGIN'
url_challenge = 'http://www.frenchtorrentdb.com/?section=LOGIN&challenge=1'
url_search    = 'http://www.frenchtorrentdb.com/?section=TORRENTS&exact=1&name=%s&submit=GO'
url_login     = 'http://www.frenchtorrentdb.com/?section=LOGIN&ajax=1'

#username, password = ('tototiti', 'Mm5/RrrFgOgR23zK')
username, password = ('tototiti', '42klm256')


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
        self._name   = 'frenchtorrentdb'
        self._cookie = None        

    def _set_cookie(self):
        header, page = self.request(url_cookie)
        self._cookie = header['Set-Cookie'].split(';')[0]

    def _get_challenge(self, headers):
        _, page = self.request(url_challenge, headers)

        jscode = PyV8.JSContext()
        jscode.enter()
        jscode.eval("var sec=%s" % page)
        r = jscode.eval("sec")

        hash = r.hash
        size = len(r.challenge)

        r.challenge[size - 1] = "'%s'" % '05f'
        secure_login_ob = "[%s]" % ','.join(r.challenge)

        r = jscode.eval(secure_login_ob)
        
        return (hash, ''.join(r))

    def _login(self):
        self._set_cookie()        
        headers = {'Cookie'           : self._cookie,
                   'Accept'           : 'application/json, text/javascript, */*; q=0.01',
                   'X-Requested-With' : 'XMLHttpRequest'}

        hash, secure_login = self._get_challenge(headers)
        params = urllib.urlencode({'username'     : username,
                                   'password'     : password,
                                   'secure_login' : secure_login,
                                   'hash'         : hash})

        headers['Content-Length'] = len(params)
    
        self.request(url_login, headers = headers, params = params)

    def _get_results_from_page(self, url_page, parser):
        _, page = self.request(url_page, headers = {'Cookie': self._cookie})

        parser.feed(page)
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
        results = list()
        _, page = self.request(url_search % filename, headers = {'Cookie': self._cookie})

        p = ParserSearch()
        p.feed(page)
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
        u = urlparse.urlparse(url_login)
        return "%s://%s" % (u.scheme, u.netloc)

    def get(self, filename):
        if not self._cookie:
            self._login()

        return self._search(filename)
