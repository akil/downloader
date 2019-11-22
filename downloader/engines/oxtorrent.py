# -*- coding: utf-8 -*-

import cfscrape
import urlparse
from lxml import etree

import os
import engine


class Oxtorrent(engine.Engine):

    def __init__(self):

        self._name    = 'oxtorrent'
        self._session = None

    def _results(self, pagetree):

        res = list()
        for item in pagetree.xpath('//table[@class="table table-hover"]/tbody/tr'):

            cells = item.xpath('td')

            if len(cells) != 4: continue

            link  = cells[0].xpath('a').pop()

            seed     = int(cells[2].xpath('text()').pop().strip())
            filename = link.text
            torlink  = urlparse.urljoin(self._config['url-root'], link.get('href'))

            query   = self._session.get(torlink, verify=False)
            tortree = etree.HTML(query.content)
            query.close()

            dlclass = tortree.xpath('//div[@class="btn-download"]').pop()
            dllink  = dlclass.xpath('a').pop().get('href')

            url = urlparse.urljoin(self._config['url-root'], dllink)

            res.append({
                'filename' : filename,
                'url'      : url,
                'seed'     : seed
            })

        return res

    def _search(self, filename):

        query   = filename.replace('.', ' ')
        payload = {'torrentSearch' : query}

        url_search = self._config['url-root']

        p = self._session.post(url_search, data = payload, verify=False)
        p.close()

        tree  = etree.HTML(p.content)
        res   = self._results(tree)

        return res

    def name(self):

        return self._name

    def url(self):

        return self._config['url-root']

    def get(self, filename, config):

        self._config  = config
        self._session = cfscrape.create_scraper()

        return self._search(filename), self._session
