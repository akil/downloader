# -*- coding: utf-8 -*-

import json
import requests
import urlparse
import HTMLParser

from lxml import etree

import engine


url_root     = 'http://www.qctorrent.io'
url_login    = 'http://www.qctorrent.io/login'
url_search   = 'http://www.qctorrent.io/retrieve_search.php'
url_download = 'http://www.qctorrent.io/dl'

username, password = ('flexsdr', 'aa4cd0eeac820c')

class Qctorrent(engine.Engine):

    def __init__(self):

        self._name    = 'qctorrent'
        self._session = None


    def _login(self):

        payload = {
            'login-username' : username,
            'login-password' : password,
            'login' : ''
        }

        s = requests.Session()
        r = s.post(url_login, payload)

        self._session = s


    def _search(self, filename):

        payload = {
            'search_string' : "%%%s%%" % filename,
            'page'          : 1,
            'aid'           : self._session.cookies.get('QcTID'),
            'order'         : 0,
            'filter'        : 0
        }

        r = self._session.post(url_search, payload, proxies = {'http' : 'http://localhost:8080'})
        r.close()

        html    = HTMLParser.HTMLParser()
        raw     = html.unescape(r.text.encode('utf-8'))
        tree    = etree.HTML(raw)
        results = list()
        
        for item in tree.xpath('//a[contains(@href,"torrent")]'):

            link = item.get('href')
            url  = urlparse.urljoin(url_download, '/'.join(link.split('/')[2:]))
            
            results.append({
                'filename' : item.text,
                'url'      : url,
                'seed'     : 0
            })

        for idx, item in enumerate(tree.xpath("//span[contains(@class,'green')]/text()[1]")):

            results[idx]['seed'] = int(item)

            
        return results


    def name(self):

        return self._name


    def url(self):

        return url_root


    def get(self, filename):

        if self._session == None:
            self._login()

        return self._search(filename), self._session
