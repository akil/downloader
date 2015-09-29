# -*- coding: utf-8 -*-

from lxml import etree
import requests
import urlparse

from engine import Engine


url_root   = 'http://www.t411.in'
url_login  = 'http://www.t411.in/users/login'
url_search = 'http://www.t411.in/torrents/search/?search=%s'

username, password = ('timeout', 'Mm5/RrrFgOgR23zK')

class T411(Engine):
    def __init__(self):

        self._name    = 't411'
        self._session = None


    def _login(self):

        payload = {
            'login'    : username,
            'password' : password,
            'remember' : 0
        }

        s = requests.session()
        r = s.post(url_login, payload)

        self._session = s

        
    def _search(self, filename):

        r = self._session.get(url_search % filename)

        results = list()
        
        tree = etree.HTML(r.text.encode('utf8'))
        for item in tree.xpath('//table/tbody/tr'):
            a = item.xpath('td/a')
            l = item.xpath('td[3]/a')
            s = item.xpath('td[8]')

            filename = a[1].get('title')
            url      = urlparse.urljoin(url_root,
                                        l[0].get('href').replace('/nfo/', '/download/'))
            seed     = s[0].text

            results.append({
                'filename' : filename.encode('utf8'),
                'url'      : url,
                'seed'     : seed
            })

        return results

    
    def name(self):

        return self._name

    def url(self):

        return url_root

    def get(self, filename):
        if self._session is None:
            self._login()

        return self._search(filename), self._session
