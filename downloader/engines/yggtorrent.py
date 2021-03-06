# -*- coding: utf-8 -*-

import cloudscraper
import requests
import urlparse
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import engine


class Yggtorrent(engine.Engine):
    def __init__(self):

        self._name = "yggtorrent"
        self._session = None

    def _login(self):

        payload = {
            "id": (None, self._config["username"]),
            "pass": (None, self._config["password"]),
            "ci_csrf_token": (None, ""),
        }
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
        }

        s = cloudscraper.create_scraper()

        s.get(self._config["url-root"])

        s.headers.update(
            {
                "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
                "referer": "{0}/?{1}".format(self._config["url-root"], "attempt=1"),
            }
        )
        r = s.post(
            self._config["url-login"], files=payload, headers=headers, verify=False
        )

        self._session = s

    def _search(self, filename):

        f = filename.replace(".", self._config["separator"]).replace(
            " ", self._config["separator"]
        )
        u = "%s%s" % (self._config["url-search"], f)
        r = self._session.get(u)

        results = list()

        tree = etree.HTML(r.text.encode("utf-8"))
        for item in tree.xpath('//table[@class="table"]/tbody/tr'):

            cells = item.xpath("td")

            name = cells[1].xpath("a/text()")[0]
            linkdl = cells[1].xpath("a/@href")[0]
            torid = cells[2].xpath("a/@target")[0]
            seed = int(cells[7].text)
            link = "%s/engine/download_torrent?id=%s" % (
                self._config["url-root"],
                torid,
            )

            filename = name.encode("ascii", "xmlcharrefreplace").strip()

            results.append(
                {"filename": filename.encode("utf8"), "url": link, "seed": int(seed)}
            )

        return results

    def name(self):

        return self._name

    def url(self):

        return self._config["url-root"]

    def get(self, filename, config):

        self._config = config

        if self._session is None:
            self._login()

        return self._search(filename), self._session
