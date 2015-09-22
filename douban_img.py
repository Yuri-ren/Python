# -*- coding: utf-8 -*-
import re
import string
import time
import urllib2
import requests
import useful_functions


####正则表达式匹配
###上一张以及下一张图片的页面url代码段
prev_pattern=re.compile(r'<link.*\n.*上一张',re.M)
next_pattern=re.compile(r'<link.*\n.*下一张',re.M)
####由以上URL代码段取出页面真实URL地址
geturl_pattern=re.compile(r'http[^"]*')
#####获取大图地址
full_img_pattern=re.compile(r'http.*查看原图"')

####相册的初始地址，即第一张图片地址
base_url='http://www.douban.com/photos/photo/1888254935/#image'
base_req=requests.get(base_url)
html_page=base_req.text.encode('utf-8')

####获取下一页以及获取当前页面大图的方法
def get_next_page(current_url):
	page_req=requests.get(current_url)
	page=page_req.text.encode('utf-8')
	m=next_pattern.search(page).group()
	next_page_url=geturl_pattern.findall(m)[0]
	######获取页面原图URL
	full_img_url=full_img_pattern.search(page).group().split('"')[0]
	####返回一个元组	
	return next_page_url,full_img_url
	

####下载照片的方法,保存到当前路径
def download_img(img_url):
	###根据URL获取文件名
	img_name=img_url.split('/')[-1]
	####下载图片
	req=requests.get(img_url)
	with open(img_name,'w') as temp_file:
		for temp_chunk in req.iter_content(chunk_size=1024):
			temp_file.write(temp_chunk)
	


#download_img('http://img3.douban.com/view/photo/large/public/p1888254935.jpg')
#test=get_next_page('http://www.douban.com/photos/photo/1888254935/#image')

#save_path='test.jpg'
#img_req=requests.get('http://img4.douban.com/view/photo/photo/public/p1578998027.jpg')
#with open(save_path,'wb') as temp_file:
#	for temp_chunk in img_req.iter_content(chunk_size=1024):
#		temp_file.write(temp_chunk)

