# -*- coding: utf-8 -*-

from lxml import etree
import requests
import urlparse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import engine

class Nyaa(engine.Engine):

    def __init__(self):

        self._name    = 'nyaa'
        self._session = None


    def _search(self, filename):

        s = self._config['separator']
        f = filename.replace('.', s).replace(' ', s)    
        r = self._session.get("%s%s" % (self._config['url-search'], f), verify=False)

        results = list()
  
        tree = etree.HTML(r.text.encode('utf-8'))
        for item in tree.xpath('//tbody/tr'):
            cells = item.xpath('td')
            if len(cells) == 1: continue
                       
            a = cells[1].xpath('a/text()')
            s = cells[5].xpath('text()')
            l = cells[2].xpath('a/@href')

            if not len(l): continue

            filename = a[0].encode('ascii', 'xmlcharrefreplace')
            seed     = int(s[0])
            url      = urlparse.urljoin(self._config['url-root'], l[0])

            if seed != 0:
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
            self._session = requests.session()
            
        return self._search(filename), self._session
