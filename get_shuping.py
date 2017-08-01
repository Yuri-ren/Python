#coding: utf-8

'''
add by yuri
拉取数据平台获取海外带宽每日api数据，并汇总每日带宽
'''

import time,requests,md5,datetime
import os

##需要获取域名的list
domain_list=['pl8.live.panda.tv','pl7.live.panda.tv']
##查询数据的起始时间
start_day=datetime.date.today()-datetime.timedelta(days=2)
end_day=''
print type(start_day)
os._exit(-1)

##昨天的日期格式
##近一周的日期list
##获得当天日期  因为数据平台的数据拉取不到实时数据 只能从当前天数的前2天向前查询一周的数据
#print datetime.date.today()
def GetWeekList():
	week_list=[]
	for i in range(2,9):
		day=datetime.date.today()-datetime.timedelta(days=i)
		week_list.append(day)
	##list中每一个为data object
	return week_list

##取得一周前的时间点，为查询时间段做准备，同上，从2天前开始算
def GetWeekAgoDay():
	#day_before_2_day=datetime.date.today()-datetime.timedelta(days=-2)
	#print day_before_2_day
	return datetime.date.today()-datetime.timedelta(days=9)

print GetWeekAgoDay()
os._exit(-1)

###生成鉴权的token
#temp_t=time.localtime()
#(tm_year=2017, tm_mon=8, tm_mday=1, tm_hour=13, tm_min=22, tm_sec=41, tm_wday=1, tm_yday=213, tm_isdst=0)
#时间格式要类似这个 2017-04-12:15
def GetToken():
	new_t=time.strftime("domain%Y-%m-%d:%H")
	m=md5.new()
	m.update(new_t)
	return m.hexdigest()

##获得当前token
temp_topic=GetToken()
###拼接请求的url
data_url="http://api.data.p2cdn.com/v2/topic/domain/pull/out/pro/isp/day/"+temp_topic
