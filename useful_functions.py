# -*- coding:utf-8 -*-

#####去除html页面中的tag标志
def del_tag(str):
	        pattern=re.compile(r'<.*?>')
	        list=pattern.findall(str)
	        for i in list:
	                str=str.replace(i,'')
	        return str.split(' ')[0]
