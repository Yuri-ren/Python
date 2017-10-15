#coding: utf-8

'''
add by yuri
拉取数据平台获取海外带宽每日api数据，并汇总每日带宽
'''

import time,requests,md5,datetime
from echarts import Echart,Legend,Bar,Axis
import os

###倒置一个list 为了最后填充数据使用
# temp_l=[2268.1028273066668, 1549.2366309600034, 1737.9599384799994, 1597.4116898133348, 1852.0315420533348, 3023.488939999995, 2833.0235811999987]
# print temp_l
# print list(reversed(temp_l))

##需要获取域名的list
# domain_list=['pl8.live.panda.tv','pl7.live.panda.tv']
domain_list=['pl8.live.panda.tv','xl.live-play.acgvideo.com','pl7.live.panda.tv','xy01.pull.yximgs.com','xy0-flv.live.huajiao.com','hdl61.kascend.com','xy.pull.yximgs.com','xy-hdl.v.momocdn.com','xy.flv.huya.com','get.xycdn.kuwo.cn','xylive-hdl.kascend.com','rtmp6.kascend.com','xy-ws.pull.yximgs.com']

##查询数据的起始时间
start_day=datetime.date.today()-datetime.timedelta(days=1)
end_day=datetime.date.today()-datetime.timedelta(days=7)

##昨天的日期格式
##近一周的日期list
##获得当天日期  因为数据平台的数据拉取不到实时数据 只能从当前天数的前2天向前查询一周的数据
#print datetime.date.today()
def GetWeekList():
	week_list=[]
	for i in range(1,8):
		day=datetime.date.today()-datetime.timedelta(days=i)
		week_list.append(str(day))
	##list中每一个为data object
	return week_list
current_week_list=GetWeekList()
# print current_week_list
##生成倒置的list 为了最后填充数据
print sorted(current_week_list)

##取得一周前的时间点，为查询时间段做准备，同上，从2天前开始算
def GetWeekAgoDay():
	#day_before_2_day=datetime.date.today()-datetime.timedelta(days=-2)
	#print day_before_2_day
	return datetime.date.today()-datetime.timedelta(days=9)

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

##请求全量数据的方法 返回一个json
def GetAllData(domain):
	url="http://api.data.p2cdn.com/v2/topic/domain/pull/out/pro/isp/day/"+temp_topic+"?"+"domain="+domain+"&sdate="+str(end_day)+"~"+str(start_day)
	# print url
	req=requests.get(url)
	if req.status_code !=200:
		print "请求数据平台api失败"
		os._exit(-1)
	else:
		##temp_json为返回数据 格式为list
		# print "请求数据平台api成功"
		temp_res_list=req.json()['data']
	return temp_res_list

# os._exit(-1)

###拼接请求的url
####请求近一周的pl8海外带宽数量
#data_url="http://api.data.p2cdn.com/v2/topic/domain/pull/out/pro/isp/day/"+temp_topic+"?"+"domain=pl8.live.panda.tv"+"&sdate="+str(end_day)+"~"+str(start_day)

##计算域名带宽方法
def CalBandForDomain(domain,data_list):
	##开始和结束时间
	#{'pl8.live.panda.tv':['sdate':'','band_total':'']}
	temp_result_list=[]
	res_dict={domain:temp_result_list}
	##final format
	# {'pl8.live.panda.tv': [{'2017-08-02': ''}, {'2017-08-01': ''}, {'2017-07-31': ''}, {'2017-07-30': ''}, {'2017-07-29': ''}, {'2017-07-28': ''}, {'2017-07-27': ''}]}
	for i in current_week_list:
		band_total=0
		#生成每一个日期对应的dict 最后append到temp_result_list中
		# {'2017-08-02': ''}
		temp_dict_in_list={i:''}
		for temp_data in data_list:
			if temp_data['sdate'] == i:
				if temp_data['domain']==domain:
					if int(temp_data['country']) != 47:
						#带宽求和
						# print type(temp_data['country'])
						band_total=band_total+float(temp_data['band'])
					else:
						##排除中国的带宽
						pass
				else:
					##非特定域名
					pass
			else:
				##日期匹配不上
				pass

		# print band_total
		temp_dict_in_list[i]=band_total/(1000*1000)
		# print temp_dict_in_list
		# [{'2017-08-02': ''},]
		final_band_list.append(band_total/(1000*1000))
		temp_result_list.append(temp_dict_in_list)
	# print temp_result_list
	return res_dict

print domain_list
##生成最终数据填充到echarts中
'''
{'pl8.live.panda.tv': [{'2017-08-04': 26766.375197813308}, {'2017-08-03': 26718.32377615999}, {'2017-08-02': 22132.00082202666}, {'2017-08-01': 20950.709171999984}, {'2017-07-31': 18836.00344704}, {'2017-07-30': 22798.786958239965}, {'2017-07-29': 22296.378565813324}]}
[22296.378565813324, 22798.786958239965, 18836.00344704, 20950.709171999984, 22132.00082202666, 26718.32377615999, 26766.375197813308]
'''
for i in domain_list:
	'''
	{
	            'name':'pl8.live.panda.tv',
	            'type':'line',
	            'stack': '总量',
	            'areaStyle': {'normal': {}},
	            'data':data_list
	        }
	'''
	final_domain_dict={}
	final_domain_dict['name']=i
	final_domain_dict['type']='line'
	# final_domain_dict['stack']='总量'
	final_domain_dict['areaStyle']={'normal': {}}

	final_band_list=[]
	##每个domain对应的全量信息
	temp_all_data=GetAllData(i)
	final_res=CalBandForDomain(i,temp_all_data)
	# print final_res
	# print list(reversed(final_band_list))
	final_domain_dict['data']=list(reversed(final_band_list))
	print final_domain_dict
	print ','
	# print '**********'
	##test
	# os._exit(-1)
