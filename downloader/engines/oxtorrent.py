# -*- coding: utf-8 -*-

import cfscrape
import requests
import urlparse
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import os

import engine


class Oxtorrent(engine.Engine):
    def __init__(self):

        self._name = "oxtorrent"
        self._session = None

    def _results(self, pagetree):

        res = list()
        for item in pagetree.xpath("//tbody/tr"):
            cells = item.xpath("td")

            if len(cells) != 4:
                continue

            link = cells[0].xpath("//div/a").pop()

            seed = int(cells[2].xpath("text()").pop().strip())
            filename = link.text
            torlink = urlparse.urljoin(self._config["url-root"], link.get("href"))

            query = self._session.get(torlink, verify=False)
            tortree = etree.HTML(query.content)
            query.close()

            dlclass = tortree.xpath('//div[@class="btn-download"]').pop()
            dllink = dlclass.xpath("a").pop().get("href")

            res.append(
                {
                    "filename": filename,
                    "url": urlparse.urljoin(self.url(), dllink),
                    "seed": seed,
                }
            )

        return res

    def _search(self, filename):

        p = self._session.get(self._config["url-root"], verify=False)
        p.close()

        query = filename.replace(".", " ")
        url_search = "%s%s" % (self._config["url-search"], query)

        p = self._session.get(url_search, verify=False)
        p.close()
        print p.content
        tree = etree.HTML(p.content)
        res = self._results(tree)

        return res

    def name(self):

        return self._name

    def url(self):

        return self._config["url-root"]

    def get(self, filename, config):

        self._config = config
        self._session = cfscrape.create_scraper()

        self._session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
            }
        )

        return self._search(filename), self._session
