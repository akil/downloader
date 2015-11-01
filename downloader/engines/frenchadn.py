# -*- coding: utf-8 -*-

import requests
from lxml import etree

import engine
import urlparse

username, password = ('skrillex', 'Mm5RrrFgOgR23zK')

url_root   = 'https://french-adn.com'
url_login  = 'https://french-adn.com/takelogin.php'
url_search = 'https://french-adn.com/browse.php'


class Frenchadn(engine.Engine):

    def __init__(self):

        self._name    = 'french-adn'
        self._session = None


    def _login(self):

        payload = {
            'username' : username,
            'password' : password
        }

        s = requests.Session()

        s.get(url_root, verify=False)
        s.post(url_login, data = payload, verify = False)

        self._session = s


    def _search(self, filename):

        req = {
            'keywords'    : '%s' % filename,
            'search'      : 'Rechercher',
            'search_type' : 't_name',
            'do'          : 'search',
            'section'     : 'TORRENTS',
            'group'       : ''
        }

        p = self._session.post(url_search, req)
        p.close()

        tree = etree.HTML(p.text)

        results = list()
        for item in tree.xpath('//table[@width="100%" and @border="0" and @cellpadding="0" and @cellspacing="0"]//tr'):
            n = item.xpath('td[@class="trow1" and @align="left"]/div/a')
            if len(n) == 0: continue
            d = item.xpath('td[@class="alt2" and @align="center"]/a')
            s = item.xpath('td[@class="trow1" and @align="center"]/div/font/a')

            try:
                dwl = d[1].get('href')
            except:
                continue
            
            name    = n[2].getchildren()[0].text
            try:
                seed = s[0].getchildren()[0].text
            except:
                seed = 0

            prelink = {
                'url'    : urlparse.urljoin(url_root, 'takethanks.php'),
                'method' : 'post',
                'data'   : {'torrentid' : dwl.split('?')[1].split('=')[1]}
            }

            results.append({
                'filename' : name,
                'url'      : dwl,
                'seed'     : seed,
                'prelink'  : prelink
            })


        return results


    def name(self):

        return self._name


    def url(self):

        return url_root


    def get(self, filename):

        if self._session == None:
            self._login()

        return self._search(filename), self._session
