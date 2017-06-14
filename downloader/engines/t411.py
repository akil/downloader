# -*- coding: utf-8 -*-

from lxml import etree
import requests
import urlparse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import engine


class T411(engine.Engine):
    def __init__(self):

        self._name    = 't411'
        self._session = None


    def _login(self):

        payload = {
            'login'    : self._config['username'],
            'password' : self._config['password'],
            'remember' : 1
        }

        s = requests.session()
        s.headers.update({
            'User-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"
        })
        r = s.post(self._config['url-login'], data=payload, verify=False)

        self._session = s

        
    def _search(self, filename):

        u = "%s%s" % (self._config['url-search'], filename)
        r = self._session.get(u, verify=False)

        results = list()
        
        tree = etree.HTML(r.text.encode('utf-8'))
        for item in tree.xpath('//table/tbody/tr'):
            a = item.xpath('td/a')
            s = item.xpath('td[8]')

            filename = a[1].get('title').encode('ascii', 'xmlcharrefreplace')
            link     = a[1].get('href').replace('//', 'https://')
            seed     = s[0].text
            
            pagetorrent = self._session.get(link, verify=False)
            magnetree   = etree.HTML(pagetorrent.text.encode('utf-8'))

            infohash = magnetree.xpath('//div[@class="accordion"]/div/table/tr[5]/td/text()').pop()
            
            results.append({
                'filename' : filename,
                'url'      : "magnet:?xt=urn:btih:%s" % infohash,
                'seed'     : int(seed)
            })

        return results

    
    def name(self):

        return self._name


    def url(self):

        return self._config['url-root']

    
    def get(self, filename, config):

        self._config = config
        
        if self._session is None:
            self._login()

        return self._search(filename), self._session
