# -*- coding:utf-8 -*-
import re
import string 
import urllib2
#from userful_functions import *

baseurl='http://tieba.baidu.com/p/3196294113'
see_lz='1'
pg_no='1'
url=baseurl+'?'+'see_lz='+see_lz+'&pn='+pg_no

#######取出页码总数
temp_page_count=page_count.findall(page)[0]
temp_page_count_1=del_tag(temp_page_count).split('，')[-1]
page_count=int(page_count_num.findall(temp_page_count_1)[0])
#print "当前页码总数为",page_count
#####去除html页面中的tag标志
def del_tag(str):
                pattern=re.compile(r'<.*?>')
                list=pattern.findall(str)
                for i in list:
                        str=str.replace(i,'')
                return str.split(' ')[0]

#####正则表达式匹配模式
page_count=re.compile(r'<li class.*共.*</li>')
page_count_num=re.compile(r'\d{1,}')

####取出url页面总数
#def get_page_num()

request=urllib2.Request(url)
response=urllib2.urlopen(request)
page=response.read()

