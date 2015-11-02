# -*- coding:utf-8 -*-
import re
import os

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

####去除windows创建目录时的特殊字符，例如* |等，并以空格替换
def del_str_for_win(dir_name):
	special_str_list=r'* \ / : ? < > | "'.split(' ')
	if(os.name=='nt'):
		for temp_str in special_str_list:
			if dir_name.__contains__(temp_str):
               			print u"标题含有特殊字符--->",temp_str,u"将会用空格替换!!!!"
               			dir_name=dir_name.replace(temp_str,'')
			else:
				continue
	else:
		print u"只有windows系统下创建目录无法包含特定字符~~~其他os请忽略"
	return dir_name
		
###以下是测试代码行
if (__name__='main'):
	page_title='renyouyin*de**dede??ki<>'
	print del_str_for_win(page_title)
else:
	pass
