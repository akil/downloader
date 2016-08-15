# -*- coding: utf-8 -*-

import cfscrape
import requests
from lxml import etree

import engine
import urlparse


url_root     = "http://www.cpasbien.cm/homec.php"
url_search   = "http://www.cpasbien.cm/recherche/"
url_download = "http://www.cpasbien.cm/telechargement/"


class Cpasbien(engine.Engine):

    def __init__(self):

        self._name    = 'cpasbien'
        self._session = None


    def _results(self, pagetree):

        res = list()

        items = pagetree.xpath('//div[starts-with(@class, "ligne")]')

        for idx, item in enumerate(items):
            filename = item.xpath('//a[@class="titre"]')[idx].text
            seed = item.xpath('//span[@class="seed_ok"]')[idx].text
            link = item.xpath('//a[@class="titre"]')[idx].get('href')
            
            u = urlparse.urlsplit(link).path.split('/')
            u_torrent = u[len(u) - 1].replace('.html', '.torrent')
            
            res.append({
                'filename' : filename,
                'url'      : urlparse.urljoin(url_download, u_torrent),
                'seed'     : seed
            })
            
        return res


    def _search(self, filename):

        url = urlparse.urljoin(url_search, "%s.html" % filename.replace('+', '-'))

        p = self._session.get(url)
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

