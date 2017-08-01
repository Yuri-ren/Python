#coding: utf-8

import time,requests,md5
import os

###生成鉴权的token
temp_t=time.localtime()
#(tm_year=2017, tm_mon=8, tm_mday=1, tm_hour=13, tm_min=22, tm_sec=41, tm_wday=1, tm_yday=213, tm_isdst=0)
#时间格式要类似这个 2017-04-12:15
new_t=time.strftime("domain%Y-%m-%d",temp_t)

def GetMd5sum(str):
	m=md5.new()
	m.update(str)
	return m.hexdigest()

temp_topic=GetMd5sum(new_t)

data_url="http://api.data.p2cdn.com/v2/topic/domain/pull/out/pro/isp/day/"+
