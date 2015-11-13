# -*- coding:utf-8 -*-
import requests
import os
import re

###下载http://www.topit.me/某人主页所有收藏图片
###下载某个图片专辑下的所有图片
###某个用户主页的URL格式为http://www.topit.me/user/397123,其中397123为用户ID，URL后可加参数如p=1来定位页面数

#user_homepage=raw_input('input the home page url of the user:')
#user_homepage_start=str(user_homepage)+'?p=1'

###
img_pattern=re.compile(r'<a rel="lightbox".*?</a>',re.S)
###获得用户收藏图片总页数
def get_pages(url):
	html=requests.get(url).content
	####定位页面最下方页码区域
	temp_sec_1=re.search(r'<div class="pages">.*?</div>',html)
	if(temp_sec_1):
		####定位页面链接
		page_sec=re.findall(r'<a href=.*?</a>',temp_sec_1.group())[-1]
		####最后一个即是总页数
		page_count=re.split(r'<.*?>',page_sec)[-2]
	else:
		print "用户主页收藏图片总数较少，未分页~~"
		page_count=0
	return page_count

###获取当前页面上图片跳转链接
def get_img_page(url):
	img_page_set=set()
	html=requests.get(url).content
	temp_sec=re.findall(r'<a href="http://www.topit.me/item/.*?"',html)
	for i in temp_sec:
		img_page_set.add(i.split('"')[-2])
	return img_page_set

###请求以上集合中URL，并下载图片页面中的图片
def get_img(url):
	html=requests.get(url).content
	img_url_temp=img_pattern.search(html)
	#print img_url_temp
	img_url=re.search(r'src=".*?"',img_url_temp).group().split('"')[-1]
	print img_url

if(__name__=='__main__'):
	#print get_pages('http://www.topit.me/user/397124')
#	get_img_page('http://www.topit.me/user/397123?p=1')
	#get_img('http://www.topit.me/item/28842500')
	s=requests.Session()
	s.post('')
