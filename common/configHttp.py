#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests, json
import readConfig as readConfig
# from common.Log import MyLog as Log
from Log import MyLog as Log
localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        if port:
            host = host + ':' + port
        else:
            host = host
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.cookies = requests.cookies.RequestsCookieJar()

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    def set_cookies(self,cookie):
        self.cookies = cookie

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, cookies=self.cookies, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except Exception as e:
            self.logger.error(str(e.message))
            # print(e.message)
            response = {"msg":str(e.message)}
            return json.dumps(response)


    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, cookies=self.cookies, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except Exception as e:
            self.logger.error(str(e.message))
            return str(e.message)