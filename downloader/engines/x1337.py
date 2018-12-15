# -*- coding: utf-8 -*-

import cfscrape
from lxml import etree

import urlparse
import engine

class X1337(engine.Engine):

    def __init__(self):

        self._name    = '1337x'
        self._session = None


    def _search(self, filename):

        s = self._config['separator']
        f = filename.replace('.', s).replace(' ', s)
        u = self._config['url-search'] % f
        p = self._session.get(u)

        if not len(p.text): return list()

        results = list()
        tree = etree.HTML(p.text.encode('utf-8'))
        for item in tree.xpath('//table/tbody/tr'):
            cells = item.xpath('td')
            print cells
            name     = cells[0].xpath('a')[1]
            filename = name.xpath('string(.)').strip().encode('ascii', 'xmlcharrefreplace')
            seed     = int(cells[1].xpath('string(.)').strip())
            
            dwl   = self._session.get(urlparse.urljoin(self._config['url-root'], name.values().pop()))
            dtree = etree.HTML(dwl.text.encode('utf-8'))

            link  = dtree.xpath('//a[contains(@class, "ccaaebca btn btn-deccadbf")]/@href')
            
            if len(link) == 0: continue

            l = list()
            for url in filter(lambda u: u.find('itorrents') != -1, link):
                l.append(url)

            if seed != 0:
                results.append({
                    'filename' : filename,
                    'url'      : l.pop(),
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
            self._session = cfscrape.create_scraper()
            
        return self._search(filename), self._session

