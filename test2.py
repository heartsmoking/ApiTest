#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
from common.configHttp import ConfigHttp
cfh = ConfigHttp()
params = {}
'''
from	查询起始时间戳 秒
to	查询结束时间戳 秒
topoIds(可选) <=10个 该数组为空或不填时默认所有业务系统进行查询 
streamIds(可选) 流ID数组 多个以','隔开 <=10个 该数组为空或不填时默认对所有流进行查询
monitorLevels(可选) 告警级别数组 支持查询EMERGENCY(严重)、HIGH(高)、MEDIUM(中) 、LOW(低)
选填，该数组为空或不填时默认不对告警级别条件加限制
monitorTypes(可选) 告警类型数组 暂时只支持FIXED_THRESHOLD(静态阈值)、COMBINE(复合关联)两个条件(支持条件内多个).选填，
该数组为空或不填时为默认不对告警类型条件加以限制
targetMetrics(可选)	暂时只支持_count(交易量)、_response_rate(响应率)、_no_response_count(交易未响应数)、
_success_rate(交易成功率)、_fail_count(交易失败数)、_latency_msec(交易响应时间)、customized(其他)
7个条件进行(支持条件内多个)，选填，该数组为空或不填时为默认不对告警指标条件加以限制
'''
# from=1526956200&to=1526958000&
# streamIds[]=5afc0e19e4b054b2b5d14499&
# groupByField=_trans_ref.TermNum&
# targetMetrics[]=_success_rate,_response_rate&sortMetric=_success_rate
params['from'] = "1528974940"
params['to'] = "1528975260"
params['streamIds[]'] = "5afe3bf3e4b054b2b5d5581c,"
params['topoIds[]'] = ""
params['monitorLevels[]'] = ""
params['monitorTypes'] = "FIXED_THRESHOLD"
params['targetMetrics[]'] = "_count,_success_rate,_response_rate"
# params['topN'] = "228"
#
# 组成get请求用的params
cfh.set_params(params)
url = "/ezsonar/apm/restDataApi/getTermsTopNData"
cfh.set_url(url)
rsp = cfh.get()
print(rsp)
