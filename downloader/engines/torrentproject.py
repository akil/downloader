# -*- coding: utf-8 -*-

import requests
import urlparse
from lxml import etree

import engine

class Torrentproject(engine.Engine):

    def __init__(self):

        self._name    = 'torrentproject'
        self._session = None
        self._config  = None


    def _search(self, filename):

        self._session = requests.session()

        f = filename.replace(' ', self._config['separator']).replace('.', self._config['separator'])
        p = self._session.get("%s%s" % (self._config['url-search'], f))

        tree = etree.HTML(p.text.encode('utf-8'))

        results = list()
        for item in tree.xpath('//div[@class="gac_bb"]/following-sibling::div'):
            links = item.xpath('span/a')

            if len(links) == 0: continue
            
            link     = links[0].get('href')
            filename = links[0].text.encode('ascii', 'xmlcharrefreplace')                        
            seed     = item.xpath('span[2]/text()')[0]

            r = self._session.get(urlparse.urljoin(self._config['url-root'], link))
            t = etree.HTML(r.text.encode('utf-8'))
            m = t.xpath('//div[@class="usite"]/a/@href').pop()

            results.append({
                'filename' : filename,
                'seed'     : int(seed),
                'url'      : m
            })

        return results
    
    def name(self):

        return self._name

    
    def url(self):

        return self._config['url-root']

    
    def get(self, filename, config):

        self._config = config

        return self._search(filename), self._session
