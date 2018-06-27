#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os
import codecs
import configparser
from readConfig import ReadConfig
# proDir = os.path.split(os.path.realpath(__file__))[0]
# 获取配置文件绝对路径
# proDir = os.path.dirname(os.path.abspath(__file__))
# configPath = os.path.join(proDir, "config.ini").replace("\\","/")
# fd = codecs.open(configPath, 'r', 'utf-8')
# data = fd.read()
#
#  # remove BOM
# # if data[:3] == codecs.BOM_UTF8:
# #     data = data[3:]
# file = codecs.open(configPath, "w", 'utf-8')
# file.write(data)
# file.close()
# fd.close()
#
# cf = configparser.ConfigParser()
# cf.read(configPath,'utf-8')
# port = cf.get('DATABASS','port')
# print port
# cf = ReadConfig()
# mail_pass = cf.get_email("mail_pass")
# if mail_pass:
#     print(cf.get_email("mail_pass"))
# else:
#     print('no mail_pass')
#登录
#################################################################################
from common.configHttp import ConfigHttp
from common.setCookie import SetCookie
import json
cfh = ConfigHttp()
sc = SetCookie()
#
# url = "/ezsonar/login/auth"
# cfh.set_url(url)
# print cfh.url
# data = {"username":"admin","password":"admin","product":"APM"}
# #
# # print data
# ndata = json.dumps(data)
# # sdata = json.loads(ndata)
# cfh.set_data(ndata)
# headers = {
#     'Content-Type':'application/json',
#     # 'Content-Type':'application/x-www-form-urlencoded',
# }
# cfh.set_headers(headers)
#
# req = cfh.post()
# print(req.status_code)
# # print(type(req.json(encoding='utf-8')))
# reqdic = req.json(encoding='utf-8')
# print(reqdic)
# datadic = reqdic["data"]
# print(datadic)
# if data['username'] == datadic['id_token'].encode('utf-8'):
#     print("OK")
# print(type(data['username']))
# print(type(datadic['id_token']))
# print(reqdic['state'])
# print(type(reqdic['state']))
# print(ndata)
# print type(ndata)
# print(sdata)
# print(type(sdata))


###############################################################################
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'2434',
    # 'Content-Type':'application/x-www-form-urlencoded', # 普通post  form
    'Content-Type':'application/json', # request payload
    # Cookie: _redmine_session=Yjl2Z0RWVm1tNUMxTnJiODlxUE
    # tsUWcxMmQwZGhrWnhxK25tUFI5ZnpjanlyNktrSTllWU9jclN3ZmJTQytmZjBYemhYVEFhcmo5MXpxSHV4cFlTOEhvSXlIOE81czJxdFVRVVFESldJTElsb3JmK2xWcHRzMXgxMEdVMzVxYnE4VzBQTDJvUGJwZVBwcDRIbmYvdGJldHRocDNSOUkrS3UrdkJWSDQzMU4rcDBLSDQxUUhtR01hQkRFZ3FlYkJHLS1tUGhVbmgxYiswRlRnMVF5NjQ5L2RnPT0%3D--687726a8f5ada8262c367c1b22a752369b050573
    # Host: 192.168.1.171:3000
    # Origin: http://192.168.1.171:3000
    # Referer: http://192.168.1.171:3000/login?back_url=http%3A%2F%2F192.168.1.171%3A3000%2F
    #  'Cookie':'JSESSIONID=1AE338BF0DF0A7384E9900792AB91197; JSESSIONID=94653D33825193897E3D6F349FDC294E',
    # 'Referer':'http://192.168.1.46/ezsonar/apm/visualization/line/new?metric=_count&parentLevel_0=eyJxdWVyeSI6eyJhbGFybVR5cGVzIjoiQ09NQklORSxGSVhFRF9USFJFU0hPTEQiLCJtZXRyaWNOYW1lcyI6Il9jb3VudCxfcmVzcG9uc2VfcmF0ZSxfbm9fcmVzcG9uc2VfY291bnQsX3N1Y2Nlc3NfcmF0ZSxfZmFpbF9jb3VudCxfbGF0ZW5jeV9tc2VjLGN1c3RvbWl6ZWQiLCJteUlkIjoiIiwic2V2ZXJpdHlWYWx1ZXMiOiJFTUVSR0VOQ1ksSElHSCxNRURJVU0sTE9XIiwidGltZSI6IntcInR5cGVcIjpcInJlbGF0aXZlXCIsXCJ2YWx1ZVwiOjE0NDAwfSJ9LCJwYXJhbXMiOnt9fQ%3D%3D&streamId[]=5ae17132e4b0c9133dba9040&time=%7B%22type%22%3A%22relative%22%2C%22value%22%3A14400%7D',
    # 'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
# headers = {
#     # 'Content-Type':'application/json',
#     'Content-Type':'application/x-www-form-urlencoded',
# }
cfh.set_headers(headers)
url = '/ezsonar/apm/api/getMetricValue'
data = {"topo": [{"metric": [{"name": "_count", "algorithm": "count"}], "id": ["5ad9a7ece4b0e13fa94a9770"]}], "time": {"type": "absolute", "value": [1530068220, 1530068280]}}
cfh.set_url(url)
cfh.set_data(json.dumps(data))
cookie = sc.set_cookies()
cfh.set_cookies(cookie)
req = cfh.post()
#
content = req.json()
print(req.url)
status_code = req.status_code
print "status_code: "+str(status_code)
print(content)
print(json.dumps(data))
# print(type(content))
# print(req.request.headers)
# print(req.headers)
# # print type(content)
# print type(req.json())
# cdict = json.loads(content,encoding='utf-8')
# print cdict
# dumpjson = json.dumps(req.json(),ensure_ascii=False)
#
# print dumpjson['state']
# print dumpjson.encode('utf-8')
# print type(dumpjson)
# print(req.status_code)
###############################################################################
# from common.configHttp import ConfigHttp
# import json
# import time
# import threading
# import datetime
# cfh = ConfigHttp()
# # #
# url = "/ezsonar/apm/restDataApi/getTermsTopNData"
# cfh.set_url(url)
#
# params = {}
# '''
# streamIds	流ID数组 多个以','隔开
# from	查询起始时间戳 整分钟
# to	查询结束时间戳 整分钟
# groupByField	分组查询字段 _trans_id,_trans_ref.****,_dst_ip,_src_ip,_sport,_dport,_ret_code.***
# targetMetrics(可选)	目标字段数组 _count,_success_rate,_response_rate
# sortMetric(可选)	排序字段 _count,_success_rate,_response_rate
# topN（可选）	返回前多少条数据 0-100 不推荐再大了， 默认5
# count 返回data默认都有count，所以targetMetrics可不写count
#
# '''
# # from=1526956200&to=1526958000&
# # streamIds[]=5afc0e19e4b054b2b5d14499&
# # groupByField=_trans_ref.TermNum&
# # targetMetrics[]=_success_rate,_response_rate&sortMetric=_success_rate
# params['streamIds[]'] = "5afe3bf3e4b054b2b5d5581c,"
# params['from'] = "1528974940"
# params['to'] = "1528975260"
# params['groupByField'] = "_src_ip"
# params['targetMetrics[]'] = "_success_rate,_response_rate"
# params['sortMetric'] = "_response_rate"
# # params['topN'] = "228"
# #
# # 组成get请求用的params
# cfh.set_params(params)
#
# rsp = cfh.get()
#
# # format_rsp = json.dumps(rsp,sort_keys=True, indent=4, separators=(',', ': '))
# print(cfh.params)
# print(rsp.url)
# print(rsp.status_code)
# if rsp.status_code != 200:
#     print rsp.text
# try:
#     rsp_json = rsp.json()
# except Exception as e:
#     rsp_json = {'msg':str(e.message)}
# format_rsp = json.dumps(rsp_json, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
# print(rsp.content)
#

# threads = []
# for i in range(300):
#     t = threading.Thread(target=cfh.get)
#     threads.append(t)
# stime = time.time()
# for t in threads:
#     t.setDaemon(True)
#     t.start()
# for t in threads:
#     t.join()
# ftime = time.time()
# print(ftime - stime)