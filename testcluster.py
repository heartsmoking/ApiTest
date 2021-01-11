#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: ZhaoFeng
Email: 

date: 2019/10/15 16:36
"""

from common.configHttp import ConfigHttp
# from common.setCookie import SetCookie
import json


cfh = ConfigHttp()
headers = {
    'Content-Type':'application/json',
    # 'Content-Type':'application/x-www-form-urlencoded',
}


# 10.11.3.105 加入集群
# curl -s http://10.11.3.104:7601/join?NodeAddr=10.11.3.105:7501&NodeID=105

# 获得10.11.3.104 节点的信息
# curl -w '\n' http://10.11.3.104:7601/nodestatus
#
# 获得当前集群的全体成员
# curl -w '\n' http://10.11.3.105:7601/clusters?NodeID=All
#
# 返回集群的领导者
# curl -w '\n' http://10.11.3.105:7601/leader
# cfh.url = "http://10.11.3.105:7601/leader"
# print(cfh.get().json())
# 加车
# curl --header "Content-Type: application/json" --request POST --data '{"type":"carinfo","data":["LA81F1HT3FA000030,20111111111111111130,11111111,京P5QV20,402882e0607944c801607cd988725d6d,,4028819d5b18f617015b192e432b011d,,,402882d25ddea6c7015ddeacf8700087,402882d25c0eeeed015c101333940ef3,,,2018-01-16 16:57:11,2018-05-13 14:21:50,1","LA81F1HT3FA000021,21222222222222222222222222222,京P5QV20,402882e0607944c801607cd988725d6d,,4028819d5b18f617015b192e432b011d,,,402882d25ddea6c7015ddeacf8700087,402882d25c0eeeed015c101333940ef3,,,2018-01-16 16:57:11,2018-05-13 14:21:50,1"]}' http://10.11.3.104:7000/batch
data = {
    "type":"carinfo",
    "data":[
        "LLLLF1HT3FA000030,20111111111111111130,11111111,\
京P5QV20,402882e0607944c801607cd988725d6d,,4028819d5b18f617015b192e432b011d,,,\
402882d25ddea6c7015ddeacf8700087,402882d25c0eeeed015c101333940ef3,,,\
2018-01-16 16:57:11,2018-05-13 14:21:50,1",
        "LLLLF1HT3FA000021,21222222222222222222222222222,\
京P5QV20,402882e0607944c801607cd988725d6d,,4028819d5b18f617015b192e432b011d,,,\
402882d25ddea6c7015ddeacf8700087,402882d25c0eeeed015c101333940ef3,,,\
2018-01-16 16:57:11,2018-05-13 14:21:50,1"
    ]
}
cfh.url = "http://10.11.3.104:5000/batch"
cfh.set_data(json.dumps(data))
cfh.set_headers(headers)
jsondata = cfh.post().json()
print(jsondata)



# 获取车辆信息
# curl -w ‘\n’ http://10.11.3.104:7000/carinfo?vin=LA81F1HT3FA000030

# 删车
# curl -w '\n' http://10.11.3.106:7000/delete?type=carinfo\&field=LA81F1HT3FA000030