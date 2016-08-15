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

        idx = 3
        while True:

            f_link = pagetree.xpath('//*[@id="gauche"]/div[%d]/a' % idx)
            if len(f_link) == 0: break

            try:
                seed = pagetree.xpath('//*[@id="gauche"]/div[%d]/div[2]/span' % idx)
            except IndexError:
                pass

            if len(seed) == 0: break
            
            filename = f_link[0].text
            link     = f_link[0].get('href')
            seed     = seed[0].text
                       
            path     = urlparse.urlsplit(link).path.split('/')
            path_tor = path[len(path) - 1].replace('.html', '.torrent')
            
            res.append({
                'filename' : filename,
                'url'      : urlparse.urljoin(url_download, path_tor),
                'seed'     : seed
            })            
            
            idx = idx + 1

        return res


    def _search(self, filename):

        link = "%s.html" % filename.name.replace('+', '-')
        url  = urlparse.urljoin(url_search, link)

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
