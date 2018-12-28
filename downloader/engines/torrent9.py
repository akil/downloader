# -*- coding: utf-8 -*-

import cfscrape
import urlparse
from lxml import etree

import os
import engine

class Torrent9(engine.Engine):

    def __init__(self):

        self._name    = 'torrent9'
        self._session = None


    def _results(self, pagetree):

        res = list()
        for item in pagetree.xpath('//div[@class="table-responsive"]/table/tbody/tr'):

            try:
                link = item[0].xpath('a')[0]
            except:
                continue

            rellink  = link.get('href')
            filename = link.xpath('string()')
            seed     = item[2].xpath('span')[0].text

            torurl  = urlparse.urljoin(self._config['url-root'], rellink)
            torpage = self._session.get(torurl, verify=False)
            tortree = etree.HTML(torpage.content)
            torlink = tortree.xpath('//a[@class="btn btn-danger download"]')[1]

            url = urlparse.urljoin(self._config['url-root'], torlink.get('href'))

            res.append({
                'filename' : filename,
                'url'      : url,
                'seed'     : int(seed)
            })

        return res


    def _search(self, filename):

        f = filename.replace('.', '-')
        u = "%s/%s.html" % (self._config['url-search'], f)
        p = self._session.get(u, verify=False)
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
