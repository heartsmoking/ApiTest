#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
author:zhaofeng

"""

import os
import codecs
import configparser

# proDir = os.path.split(os.path.realpath(__file__))[0]
# 获取配置文件绝对路径
proDir = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(proDir, "config.ini").replace("\\","/")
# print(configPath)

# with open(configPath,'r+') as cf:
#     data = cf.read()

class ReadConfig:
    def __init__(self):
        fd = codecs.open(configPath,'r','utf-8')
        data = fd.read()

        #  remove BOM
        # if data[:3] == codecs.BOM_UTF8:
        #     data = data[3:]
        file = codecs.open(configPath, "w",'utf-8')
        file.write(data)
        file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,'utf-8')

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_user(self,name):
        value = self.cf.get("USERINFO", name)
        return value