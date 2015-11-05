# -*- coding: utf-8 -*-
import re
import requests
import os

#print "Hello,world!!"

####re pattern 
title_pattern=re.compile(r'class="picset-title".*?[^<]*')
img_url_pattern=re.compile(r'<img  class="z-tag data-lazyload-src".*?data-lazyload-src=".*?"')

base_url=raw_input(u'需要下载的网易摄影的页面URL地址:'.encode('gbk'))

req=requests.get(base_url)
###转码为utf8就可以，此处转为gbk是为了在windows命令行下使用，防止乱码
#html_page=req.text.encode('utf8')
html_page=req.text.encode('gbk')
#print html_page

####获取当前相册标题
temp_title=title_pattern.search(html_page).group()
#print temp_title
title=temp_title.split('\n')[1].strip()
#print title
print u'当前相册名称为:',title
#os._exit(0)

####去除html标签的函数
def del_tag(str):
	return str.split('"')[-2]

#####获取图片的真实URL地址
img_url_list=img_url_pattern.findall(html_page)
###map函数处理tag格式之后获得图片的真实URL,存放在列表中
url_list=map(del_tag,img_url_list)
img_num=len(url_list)
print u'当前页面图片总数为:'.encode('gbk'),len(url_list)

####根据图片地址下载图片
###先创建图片存放目录
os.mkdir(title)

img_count=0
for i in url_list:
	###图片保存名称
	img_name=i.split('/')[-1]
	###拼接图片保存路径
	img_path='.'+'\\'+title+'\\'+img_name
	#print img_path
	img_req=requests.get(i)
	with open(img_path,'wb') as temp_file:
		for temp_chunk in img_req.iter_content(chunk_size=1024):
			temp_file.write(temp_chunk)
		img_count+=1
	print u"第",img_count,u"张图片下载完成~~~"
	if (img_count>img_num):
		break
	else:
		continue

