#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import sgmllib
import urlparse

from engine import Engine


url_login  = 'https://gks.gs/login'
url_search = 'https://gks.gs/sphinx/?%s'

username, password = ('timeout', 'o4PbfVnPbIDn8s1r')

class ParserSearch(sgmllib.SGMLParser):
    def reset(self):
        sgmllib.SGMLParser.reset(self)


class Gks(Engine):
    def __init__(self):
        self._name   = 'frenchtorrentdb'
        self._cookie = None        

    def _login(self):
        params  = urllib.urlencode({'username': username,
                                    'password': password,
                                    'login'   : '+Connexion+'})
        headers = {'Host'   : 'gks.gs',
                   'Referer': url_login}

        header, page = self.request(url_login,
                                    headers  = headers,
                                    params   = params,
                                    redirect = True)

        self._cookie = header['Cookie']
        
    def url(self):
        u = urlparse.urlparse(url_login)
        return "%s://%s" % (u.scheme, u.netloc)
    
    def name(self):
        return self._name

    def get(self, filename):
        if self._cookie is None:
            self._login()

        headers = {'Host'   : 'gks.gs',
                   'Cookie' : self._cookie}
        
        param = urllib.urlencode({'q': filename})
        header, page = self.request(url_search % param,
                                    headers = headers)
        print header, page



def main():
    g = Gks()
    g.get("naruto 221")

if __name__ == '__main__':
    main()
