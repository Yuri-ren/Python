# -*- coding: utf-8 -*-
import re
import requests
import json
import os
import threading


########淘宝页面商品详情为js动态加载，所以python抓取静态页面的方法无法获取到图片地址，采用直接抓取js地址，然后对其进行请求，得到json字符串，得到图片文件名
__author__='Yuri'

####淘宝图片地址，后续进行图片地址拼接
img_server='http://img.alicdn.com/imgextra/'


###re pattern
title_pattern=re.compile(r'<title>.*</title>') 
###修改寻找js的正则表达式,有两个，desc.alicdn.com和dsc.taobaocdn.com,任取其一都可以.注意，此处服务器与下文请求js得出的img地址相关
#js_pattern=re.compile(r'apiImgInfo:"//otds.alicdn.com/json/item_imgs.htm.*?"')
js_pattern=re.compile(r'desc.alicdn.com.[^"]*')
###由js请求结果过滤img地址的pattern
img_js_pattern=re.compile(r'img.alicdn.com.[^"]*')
js2dict_pattern=re.compile(r'{.*}',re.S)
filetype_pattern=re.compile(r'.*\..*')

#####将unicode字符转换为utf编码
def u2utf8(temp_string):
	return temp_string.encode('utf8')
	
	
	

####get html page
####根据系统,windows|linux来显示提示字符,防止乱码
platform=os.name
if(platform=='nt'):
	base_url=raw_input(u'请输入要下载的页面地址:'.encode('gbk'))
else:
	base_url=raw_input('请输入要下载的页面地址:')

req=requests.get(base_url)
html_page=req.text

###获取页面标题
####windows下无法创建带有特殊文件的目录，若为windows平台的话，去掉特殊字符再创建目录
special_str_list=r'* \ / : ? < > | "'.split(' ')
temp_title=title_pattern.search(html_page).group(0)
if (platform=='posix'):
	page_title=re.split(r'<.*?>',temp_title)[-2].encode('utf8')
	os.mkdir(page_title)
if (platform=='nt'):
	page_title=re.split(r'<.*?>',temp_title)[-2].encode('gbk')
	for temp_str in special_str_list:
		if page_title.__contains__(temp_str):
			print u"标题含有特殊字符--->",temp_str,u"将会用空格替换!!!!"
			page_title=page_title.replace(temp_str,'')
		else:
			continue
	print u'下面开始创建图片存放目录~~~'
	os.mkdir(page_title)

img_dir=page_title+'/'


##线程函数
def proc(temp_url,thread_count):
	img_name=str(temp_url).split('/')[-1]
	img_path=img_dir+img_name
	#print u"正在下载第",img_count,u"张图片"
	print u"开始下载图片---->",img_name
	print u"线程编号为:",thread_count
	img_req=requests.get(temp_url)
	with open(img_path,'wb') as temp_file:
		for temp_chunk in img_req.iter_content(chunk_size=1024):
			temp_file.write(temp_chunk)
	print img_name,u"下载完成~~~~"
	print u"编号为",thread_count,u"线程退出~~~"

####得到生成图片的js地址
js_temp=js_pattern.findall(html_page)[0]
img_js_url="http://"+str(js_temp)

###请求该js地址，获得关于图片地址json字符串
js_req=requests.get(img_js_url)
#temp_json=js_req.text.encode('utf8')
temp_json=js_req.text

###由请求js获得img地址
img_url_list=img_js_pattern.findall(temp_json)

###map,拼接请求的img地址
def img_url_map(temp_url):
	img_url="http://"+temp_url
	return img_url
##最终得到的img地址列表
img_url=map(img_url_map,img_url_list)
#print img_url
##图片总数
img_num=len(img_url)

####下载图片文件
#img_count=1
###图片存放目录，均为当前标题目录
#print img_dir
print u"当前页面商品图片总数为",img_num

thread_count=0
for i in img_url:
	thread_count+=1
	t=threading.Thread(target=proc,args=(i,thread_count))
	t.start()
