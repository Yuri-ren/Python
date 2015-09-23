# -*- coding: utf-8 -*-
import re
import string
import urllib2
import requests

__author__='Yuri'

####正则表达式匹配
###下一张图片的页面url代码段
next_pattern=re.compile(r'<link.*\n.*下一张',re.M)
####由以上URL代码段取出页面真实URL地址
geturl_pattern=re.compile(r'http[^"]*')
#####获取大图地址
full_img_pattern=re.compile(r'http.*查看原图"')
####获取默认页面图片
def_img_pattern=re.compile(r'<a class="mainphoto".*?http.*?http.*?"',re.S)

####相册的初始地址，即第一张图片地址
####相册的初始地址也可以作为相册遍历的停止条件，若下一张的地址为该baseurl的话，则相册图片遍历终止
base_url=raw_input('输入要下载的豆瓣相册的第一张图片URL:')
begin_url=base_url
base_req=requests.get(base_url)
html_page=base_req.text.encode('utf-8')

def get_next_page(current_url):
        page_req=requests.get(current_url)
        page=page_req.text.encode('utf-8')
        m=next_pattern.search(page).group()
        next_page_url=geturl_pattern.findall(m)[0]
        ######获取页面原图URL,无原图则下载默认页面
        temp_section=full_img_pattern.search(page)
        if temp_section:
                full_img_url=temp_section.group().split('"')[0]
                def_img_url=def_img_pattern.search(page).group().split('"')[-2]
        else:
                full_img_url=''
                def_img_url=def_img_pattern.search(page).group().split('"')[-2]
        ####返回一个元组 第一个元素为下一页的URL,第二个元素为原图片地址（方便确定文件名称）,第三个为大图页面地址（为空表示该图片无大图）
        return next_page_url,def_img_url,full_img_url


####下载照片的方法,保存到当前路径
def download_img(img_url):
	###根据URL获取文件名
	img_name=img_url.split('/')[-1]
	####下载图片
	req=requests.get(img_url)
	with open(img_name,'wb') as temp_file:
		for temp_chunk in req.iter_content(chunk_size=1024):
			temp_file.write(temp_chunk)
####下载原图的方法
def download_full_img(str1,str2):
	full_img_pattern=re.compile(r'<td id="pic-viewer.*?jpg',re.S)
        img_name=str1.split('/')[-1]
	####str2只是大图页面的地址,还要进一步用re捕获图片地址
        temp_req=requests.get(str2)
	temp_section=full_img_pattern.search(temp_req.text.encode('utf-8')).group()	
	full_img_url=temp_section.split('"')[-1]
	req=requests.get(full_img_url)
        #img_full_url=str2
        with open(img_name,'wb') as temp_file:
                for temp_chunk in req.iter_content(chunk_size=1024):
                        temp_file.write(temp_chunk)
	
img_count=0
while True:
	temp_tuple=get_next_page(base_url)
	next_page=temp_tuple[0]
	if (temp_tuple[2]==''):
		download_img(temp_tuple[1])
		img_count+=1
	else:
		download_full_img(temp_tuple[1],temp_tuple[2])
		img_count+=1
	if (next_page==begin_url):
		print "当前相册全部下载完成，退出....."	
		print "当前相册图片总数为:",img_count
		break
	else:
		print "开始下载下一张图片~~~~~~"
		base_url=next_page
		continue
