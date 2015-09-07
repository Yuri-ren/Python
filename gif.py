# -*- coding:utf-8 -*-
import re
import string 
import urllib2
import useful_functions

baseurl='http://tieba.baidu.com/p/3196294113'
#baseurl='http://tieba.baidu.com/p/3949977663'
####是否只看LZ
see_lz='1'
###初始页码
pg_no=1

#####获取页码总数
page_count=re.compile(r'<li class.*共.*</li>')
page_count_num=re.compile(r'\d{1,}')
page_request=urllib2.Request(baseurl)
page_response=urllib2.urlopen(page_request)
page_html=page_response.read()
temp_page_count=page_count.findall(page_html)[0]
temp_page_count_1=useful_functions.del_tag(temp_page_count).split('，')[-1]
####页码总数
page_count=int(page_count_num.findall(temp_page_count_1)[0])
print "当前页面总数为:",page_count

while True:
	print "正在下载第",pg_no,"页的gif......"
	#####拼接URL字符串
	url=baseurl+'?'+'see_lz='+see_lz+'&pn='+str(pg_no)
	####获取html页面
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	page=response.read()
	
	print pg_no
	pg_no=pg_no+1
	if pg_no >page_count:
		print "全部页面下载完成，退出"
		break
	else:
		continue
