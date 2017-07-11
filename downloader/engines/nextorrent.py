# -*- coding: utf-8 -*-

from lxml import etree
import requests
import urlparse
import logging

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import engine


_LOG = logging.getLogger(__name__)


class Nextorrent(engine.Engine):

    def __init__(self):

        self._name    = 'nextorrent'
        self._session = None


    def _login(self):

        payload = {
            'user'   : self._config['username'],
            'pass'   : self._config['password'],
            'submit' : 'submit'
        }

        s = requests.session()
        r = s.post(self._config['url-login'], payload, verify=False)

        self._session = s


    def _search(self, filename):

        p = {'torrentSearch': filename.replace('.', self._config['separator'])}
        r = self._session.post(self._config['url-search'], p, verify=False)

        results = list()

        tree = etree.HTML(r.text.encode('utf-8'))
        for item in tree.xpath('//table/tbody/tr'):
            cells = item.xpath('td')

            if len(cells) == 1: return results

            a = cells[0].xpath('a/text()')
            s = cells[2].xpath('text()')
            l = cells[0].xpath('a/@href')
            d = urlparse.urljoin(self._config['url-root'], l[0])

            page = self._session.get(d)
            res  = etree.HTML(page.text.encode('utf-8'))

            dl_tor = res.xpath('//div[@class="download"]/div[contains(@class, "btn-download")]/a/@href')
            dl_mag = res.xpath('//div[@class="download"]/div[contains(@class, "btn-magnet")]/a/@href')
            
            filename = a[0].encode('ascii', 'xmlcharrefreplace')
            seed     = int(s[0].strip())
            
            if seed == 0: continue

            if len(dl_mag):
                dl = dl_mag.pop()
            elif len(dl_tor):
                dl = dl_tor.pop()
            else:
                _LOG.error("engine:%s link:ko" % self._name)
                continue                
                
            url = urlparse.urljoin(self._config['url-root'], dl)
            
            results.append({
                'filename' : filename,
                'url'      : url,
                'seed'     : seed
            })

        return results


    def name(self):

        return self._name

    def url(self):

        return self._config['url-root']


    def get(self, filename, config):

        self._config = config

        if self._session is None:
            self._login()

        return self._search(filename), self._session
