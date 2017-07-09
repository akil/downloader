# -*- coding: utf-8 -*-

from lxml import etree
import requests
import urlparse

import engine

class X1337(engine.Engine):

    def __init__(self):

        self._name    = '1337x'
        self._session = None


    def _search(self, filename):

        s = self._config['separator']
        f = filename.replace('.', s).replace(' ', s)
        p = self._session.get("%s%s" % (self._config['url-search'], f))

        results = list()

        tree = etree.HTML(p.text.encode('utf-8'))
        for item in tree.xpath('//table/tbody/tr'):
            cells = item.xpath('td')

            if len(cells) != 6: continue

            name     = cells[0].xpath('a')[1]
            filename = name.xpath('string(.)').strip().encode('ascii', 'xmlcharrefreplace')
            seed     = cells[1].xpath('string(.)').strip()

            dwl   = self._session.get(urlparse.urljoin(self._config['url-root'], name.values().pop()))
            dtree = etree.HTML(dwl.text.encode('utf-8'))

            link  = dtree.xpath('//a[contains(@class, "btn-magnet")]/@href')

            if len(link) == 0: continue

            if seed != 0:
                results.append({
                    'filename' : filename,
                    'url'      : link.pop(),
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
            self._session = requests.session()


        return self._search(filename), self._session
