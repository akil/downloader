# -*- coding:utf-8 -*-

import requests
from lxml import etree

import engine


username, password = ('outkast', 'Mm5/RrrFgOgR23zK')

url_root   = 'http://smartorrent.com'
url_login  = 'http://smartorrent.com/login'
url_search = 'http://smartorrent.com/executeSearch'


class Smartorrent(engine.Engine):

    def __init__(self):

        self._name   = 'smartorrent'
        self._cookie = None


    def _login(self):

        payload = {
            'username' : username,
            'password' : password
        }

        r = requests.post(url_login, payload)

        self._cookie = r.headers['set-cookie']        

        r.close()

        
    def _search(self, filename):

        r = requests.post(url_search,
                          headers = {'Cookie' : self._cookie},
                          data = {'keywords' : filename})
        r.close()

        results = list()
        
        tree = etree.HTML(r.text.encode('utf8'))
        for item in tree.xpath('//div[@class="list-group"]/a'):
            link = item.get('href')
            name = item.xpath('h5/strong')
            seed = item.xpath('p/span[@class="pull-right"]/span[@class="label label-success"]')

            results.append({
                'filename' : name[0].text,
                'url'      : link.replace('/torrents/', '/download/'),
                'seed'     : seed
            })
            
        return results
            
        
    def name(self):

        return self._name

    
    def url(self):

        return url_root

    
    def get(self, filename):

        if self._cookie == None:
            self._login()

        return self._search(filename), self._cookie
