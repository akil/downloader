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
        u = "%s%s" % (self._config['url-search'], f)
        r = self._session.get(u, verify=False)

        results = list()

        tree = etree.HTML(r.text.encode('utf-8'))
        for item in tree.xpath('//tbody/tr'):
            cells = item.xpath('td')
            if len(cells) == 1: continue

            n = cells[1].xpath('a/text()')
            if len(n) == 1:
                name = n[0]
            else:
                name = n[2]

            link = urlparse.urljoin(
                self._config['url-root'],
                cells[2].xpath('a/@href')[0])
            seed = int(cells[5].xpath('text()')[0])
            filename = name.encode('ascii', 'xmlcharrefreplace')
            print link
            if seed != 0:
                results.append({
                    'filename' : filename,
                    'url'      : link,
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
