# -*- coding: utf-8 -*-

import cfscrape
from lxml import etree

import engine
import urlparse


url_root     = "http://www.torrent9.biz/"
url_search   = "http://www.torrent9.biz/search_torrent/"
url_download = "http://www.torrent9.biz/get_torrent/"


class Torrent9(engine.Engine):

    def __init__(self):

        self._name    = 'torrent9'
        self._session = None


    def _results(self, pagetree):


        res = list()

        for item in pagetree.xpath('//div[@class="table-responsive"]/table/tbody/tr'):

            link = item[0].xpath('a')[0]

            rellink  = link.get('href')
            filename = link.xpath('string()')
            seed     = item[2].xpath('span')[0].text

            url = "%s.torrent" % urlparse.urljoin(url_download, rellink)

            res.append({
                'filename' : filename,
                'url'      : url,
                'seed'     : seed
            })

        return res


    def _search(self, filename):
        
        f    = filename.name.replace('+', ' ').replace('.', ' ')        
        data = {
            'champ_recherche' : f
        }

        h = {
            'User-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"
        }
        
        p = self._session.post(url_search, headers=h, data=data)
        p.close()

        tree  = etree.HTML(p.content)
        res   = self._results(tree)

        return res


    def name(self):

        return self._name


    def url(self):

        return url_root


    def get(self, filename):

        self._session = cfscrape.create_scraper()

        return self._search(filename), self._session
