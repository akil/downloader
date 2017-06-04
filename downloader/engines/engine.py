# -*- coding: utf-8 -*-


class Engine(object):    

    def url(self):
        raise NotImplementedError("Implementation of engine url")

    def name(self):
        raise NotImplementedError("Implementation of engine name")
    
    def get(self, filename):
        raise NotImplementedError("Implementation of file downloading")
