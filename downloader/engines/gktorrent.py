# -*- coding: utf-8 -*-

import requests
import urlparse
from lxml import etree

import engine

class Gktorrent(engine.Engine):

    def __init__(self):

        self._name    = 'gktorrent'
        self._session = None


    def _search(self, filename):

        f = filename
        for c in ['-', '.', '+', ' ']:
            f = f.replace(c, self._config['separator'])

        url = urlparse.urljoin(self._config['url-search'], f)
        
        query = self._session.get(url)
        query.close()
        pagetree = etree.HTML(query.content)

        results = list()
        for item in pagetree.xpath('//table[@class="table table-hover"]/tbody/tr'):

            cells = item.xpath('td')

            if len(cells) != 4: continue

            filename = cells[0].xpath('a/text()')[0]
            dlurl    = cells[0].xpath('a/@href')[0]
            seed     = cells[2].xpath('text()')[0]
            
            
            q = self._session.get(urlparse.urljoin(self._config['url-root'], dlurl))
            q.close()

            torpage = etree.HTML(q.content)
            link    = torpage.xpath('//div[@class="downloading"]/div/a')[0]

            url = urlparse.urljoin(self._config['url-root'], link.get('href'))
            
            results.append({
                'filename' : filename,
                'url'      : url,
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
            self._session.verify = False

        return self._search(filename), self._session
