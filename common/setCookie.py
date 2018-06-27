#! /usr/bin/env python
# -*- coding:utf-8 -*-

from readConfig import ReadConfig
import requests,json
import re
localReadConfig = ReadConfig()

class SetCookie:
    def __init__(self):
        global user,password,baseurl
        user = localReadConfig.get_user("user")
        password = localReadConfig.get_user("password")
        baseurl = localReadConfig.get_http("baseurl")
        self.cookies = requests.session().cookies
        self.auurl = "/ezsonar/login/auth"
        self.appurl = "/ezsonar/apm/apps"

    def set_cookies(self):
        self.data = {"username":user,"password":password,"product":"APM"}
        self.headers = {
            'Content-Type':'application/json',
            'Connection':'keep-alive'
            # 'Content-Type':'application/x-www-form-urlencoded',
            }
        self.aurl = baseurl+":"+"81"+ self.auurl
        req = requests.post(self.aurl, data=json.dumps(self.data), headers=self.headers)
        print(req.status_code)
        datadic = req.json()
        redirect = datadic['data']['redirect']
        token = re.search(r'(?=\?).*', redirect).group()
        cookie1 = req.cookies
        appurl = baseurl+self.appurl + token
        request = requests.get(appurl)
        cookie2 = request.cookies
        self.cookies.update(cookie1)
        self.cookies.update(cookie2)
        return self.cookies