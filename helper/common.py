#!/usr/bin/env python3


### Importing Common stuffs
import json
from urllib import request as req
from bs4 import BeautifulSoup


### Common data
class CommonThings:

    def __init__(self):
        self.headers = {
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }

    def requestToWeb(self, url, beautify = True, **kwargs):
        if kwargs:
            self.headers.update(kwargs)
        self.request = req.Request(
            url,
            headers = self.headers
        )
        res = req.urlopen(self.request)
        self.webcontent = res.read()
        if beautify:
            self.parsedData = BeautifulSoup(self.webcontent, 'html.parser')
            return self.parsedData
        else:
            return self.webcontent

