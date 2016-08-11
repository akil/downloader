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

        headers = {
            'Host': 'qctorrent.io',
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip, deflate',
            'Referer' : 'http://qctorrent.io/login',
            'Content-Type' : 'application/x-www-form-urlencoded'
        }
        
        payload = {
            'login-username' : username,
            'login-password' : password,
            'login' : ''
        }
        
        s = requests.session()
        s.get(url_root)
        
        r = s.post(url_login, payload, headers = headers)

        self._session = s
        

        
    def _search(self, filename):

        results = list()
        payload = {
            'search_string' : "%%%s%%" % filename,
            'page'          : 1,
            'aid'           : self._session.cookies.get('QcTID'),
            'order'         : 0,
            'filter'        : 0,
            'categories'    : '',
        }

        r = self._session.post(url_search, payload)
        r.close()
        
        if len(r.text) == 0:
            return results
       
        html    = HTMLParser.HTMLParser()
        raw     = html.unescape(r.text.encode('utf-8'))
        tree    = etree.HTML(raw)
        
        for item in tree.xpath('//a[contains(@href,"torrent")]'):

            link     = item.get('href')
            filename = item.text
            url      = urlparse.urljoin(url_download,
                                        '/'.join(link.split('/')[2:]))
            
            results.append({
                'filename' : filename,
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
