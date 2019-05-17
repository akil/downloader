# -*- coding: utf-8 -*-

from lxml import etree

import requests
import urlparse
import engine

class Cpasbien(engine.Engine):

    def __init__(self):

        self._name    = 'cpasbien'
        self._session = None


    def _search(self, filename):

        u = self._config['url-search'] % filename
        p = self._session.get(u)

        if not len(p.text): return list()

        print p.text
        # results = list()
        # tree = etree.HTML(p.text.encode('utf-8'))
        # for item in tree.xpath('//table/tbody/tr'):
        #     cells = item.xpath('td')

        #     name     = cells[0].xpath('a')[1]
        #     filename = name.xpath('string(.)').strip().encode('ascii', 'xmlcharrefreplace')
        #     seed     = int(cells[1].xpath('string(.)').strip())

        #     dwl   = self._session.get(urlparse.urljoin(self._config['url-root'], name.values().pop()))
        #     dtree = etree.HTML(dwl.text.encode('utf-8'))

        #     link  = dtree.xpath('//a[contains(@class, "ccaaebca btn btn-deccadbf")]/@href')

        #     if len(link) == 0: continue

        #     l = list()
        #     for url in filter(lambda u: u.find('itorrents') != -1, link):
        #         l.append(url)

        #     if seed != 0:
        #         results.append({
        #             'filename' : filename,
        #             'url'      : l.pop(),
        #             'seed'     : int(seed) 
        #         })

        # return results


    def name(self):

        return self._name


    def url(self):

        return self._config['url-root']


    def get(self, filename, config):

        self._config = config

        if self._session is None:
            self._session = requests.session()
            self._session.verify = False

        return self._search(filename), self._session 



if __name__ == '__main__':

    config = dict()
    config['url-root']   = 'http://cpasbien.cm'
    config['url-search'] = 'http://cpasbien.cm/recherche/%s'

    c = Cpasbien()
    c.get("empire S05E01", config)
