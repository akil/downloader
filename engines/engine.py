#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

class Engine(object):
    def url(self):
        raise NotImplementedError("Implementation of engine url")

    def name(self):
        raise NotImplementedError("Implementation of engine name")
    
    def get(self):
        raise NotImplementedError("Implementation of file downloading")

    def request(self, url, headers = None, params = None):
        if headers is not None and params is not None:
            req = urllib2.Request(url, headers = headers, data = params)
        elif headers is not None:
            req = urllib2.Request(url, headers = headers)
        elif params is not None:
            req = urllib2.Request(url, data = params)
        else:
            req = urllib2.Request(url)

        page   = urllib2.urlopen(req)
        header = page.info()
        data   = page.read()

        page.close()

        return (header, data)
