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
            l = item.xpath('td[3]/a')
            s = item.xpath('td[8]')

            filename = a[1].get('title').encode('ascii', 'xmlcharrefreplace')
            url      = urlparse.urljoin(self._config['url-root'],
                                        l[0].get('href').replace('/nfo/', '/download/'))
            seed     = s[0].text

            results.append({
                'filename' : filename,
                'url'      : url,
                'seed'     : seed
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
