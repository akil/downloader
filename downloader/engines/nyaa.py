# -*- coding: utf-8 -*-

import requests
from lxml import etree

import engine

url_root   = "http://nyaa.se"
url_search = "http://www.nyaa.se/?page=search&cats=1_0&filter=0&term=%s"

class Nyaa(engine.Engine):

    def __init__(self):

        self._name    = 'nyaa'
        self._session = None


    def _get_results(self, pagetree):

        res = list()

        for item in pagetree.xpath('//tr[@class="tlistrow"]'):

            name = item.xpath('td[@class="tlistname"]/a')[0].text.encode('ascii', 'xmlcharrefreplace')
            seed = item.xpath('td[@class="tlistsn"]')
            link = item.xpath('td[@class="tlistdownload"]/a')[0].get('href')

            if len(seed) == 0:
                seed = 0
            else:
                seed = seed[0].text
                
            res.append({
                'filename' : name,
                'url'      : link,
                'seed'     : seed
            })

        return res

    
    def _search(self, filename):

        s = requests.Session()
        r = s.get(url_search % filename)
        r.close()

        self._session = s
        
        tree  = etree.HTML(r.text.encode('utf8'))
        res   = self._get_results(tree)
        pages = tree.xpath('//div[@class="pages"]/a/@href')
        
        if len(pages) == 0:
            return res
        else:
            respages = list()

            respages.extend(res)

            for page in pages:

                r = self._session.get(page)
                r.close()

                tree = etree.HTML(r.text.encode('utf8'))
                respages.extend(self._get_results(tree))

        return respages

    
    def name(self):
        
        return self._name
    

    def url(self):

        return url_root
    

    def get(self, filename):

        return self._search(filename), self._session
