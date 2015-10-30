# -*- coding:utf-8 -*-
import re

#####去除html页面中的tag标志
def del_tag(str):
        pattern=re.compile(r'<.*?>')
        list=pattern.findall(str)
        for i in list:
                str=str.replace(i,'')
        return str.split(' ')[0]

####由html便签中取出资源url地址
def get_url_from_html(s):
	pattern=re.compile(r'http://.*?"')
	temp_url=pattern.findall(s)[0]
	url=temp_url.split('"',1)[0]
	return url

####下载资源的方法
def download(temp_url,file_path):
	pass	
