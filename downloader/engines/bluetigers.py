#! -*- coding: utf-8 -*-

import requests
import urlparse
from lxml import etree

import engine

url_root     = 'https://www.bluetigers.ca'
url_login    = 'https://www.bluetigers.ca/account-login.php'
url_search   = 'https://www.bluetigers.ca/torrents-search.php?search=%s&incldead=0&freeleech=0&lang=0'
url_download = 'https://www.bluetigers.ca/download.php?id=%s'

username, password = ('timeout', 'ebC1TtTgs8HwExl3')

passkey='a4fc87b69bbfa311990c813d54d07264'


class Bluetigers(engine.Engine):

    def __init__(self):

        self._name    = 'bluetigers'
        self._session = None


    def _login(self):

        payload = {
            'take_login' : 1,
            'username'   : username,
            'password'   : password
        }

        s = requests.Session()
        s.headers.update({
            'User-Agent'     : 'Mozilla/5.0 (X11; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
            'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'None'
        })
      
        s.post(url_login, payload, verify=False)

        self._session = s


    def _pages(self, tree):

        pages = list()
        for link in tree.xpath('//a'):
            h = link.get('href')
            if not h: continue
            if h.find('page') == -1: continue

            url = urlparse.urljoin(url_root, h)
            if not url in pages: pages.append(url)


        return pages


    def _get_torrents(self, tree):

        results = list()
        for item in tree.xpath('//table[@class="ttable_headinner"]//tr'):
            a = item.xpath('td[@class="ttable_col2" and @nowrap="nowrap"]/a[2]')
            f = item.xpath('td[@class="ttable_col2"]//b//font/b')

            text = a[0].getchildren()[0].text
            link = url_download % a[0].get('href').split('&')[0].split('=')[1]
            seed = f[0].text

            results.append({
                'filename' : text,
                'url'      : link,
                'seed'     : seed
            })

        return results


    def _search(self, filename):

        p = self._session.get(url_search % filename, verify=False)

        tree  = etree.HTML(p.text)
        pages = self._pages(tree)

        torrents = list()
        res      = self._get_torrents(tree)

        if len(res): torrents.extend(res)

        for page_url in pages:

            p = self._session.get(page_url, verify=False)

            tree = etree.HTML(p.text)
            res  = self._get_torrents(tree)

            if len(res) : torrents.extend(res)

        return torrents


    def name(self):

        return self._name


    def url(self):

        u = urlparse.urlparse(url_login)
        return "%s://%s" % (u.scheme, u.netloc)


    def get(self, filename):

        if self._session == None:
            self._login()

        return self._search(filename), self._session
