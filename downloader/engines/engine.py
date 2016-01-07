#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        uid, pw = None, None

        for _,item in enumerate(headers.get('Set-Cookie').split(';')):
            item = item.strip()
            if item.find(',') != -1:
                for _,i in enumerate(item.split(',')):
                    i = i.strip()
                    if 'pw' in i.split('='): pw = i
            else:
                if 'uid' in item.split('='): uid = item
 
        ret = urllib2.HTTPRedirectHandler.http_error_302(self,
                                                         req,
                                                         fp,
                                                         code,
                                                         msg,
                                                         headers)
        
        ret.headers['Cookie'] = '%s; %s' % (uid, pw)
        return ret


class Engine(object):    
    def url(self):
        raise NotImplementedError("Implementation of engine url")

    def name(self):
        raise NotImplementedError("Implementation of engine name")
    
    def get(self, filename):
        raise NotImplementedError("Implementation of file downloading")

    def request(self, url, headers = None, params = None, redirect = False):
        if headers is not None and params is not None:
            req = urllib2.Request(url, headers = headers, data = params)
        elif headers is not None:
            req = urllib2.Request(url, headers = headers)
        elif params is not None:
            req = urllib2.Request(url, data = params)
        else:
            req = urllib2.Request(url)

        if redirect:
            opener = urllib2.build_opener(RedirectHandler())
            page   = opener.open(req)
        else:
            page   = urllib2.urlopen(req)

        header = page.info()
        data   = page.read()

        page.close()

        return (header, data)
