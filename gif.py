# -*- coding:utf-8 -*-
import re
import urllib2
import urllib
import useful_functions
import time
import requests

__author__='Yuri'
####windows下命令行会出现中文乱码，我的解决方法是直接使用Unicode字符，然后encode('gbk')进行转码
#####下载百度贴吧url页面中的gif，自动遍历所有页面抓取
#####see_lz变量控制是否只看LZ

####根据网页URL获取网页源代码的class
class HTML():
        def __init__(self,url):
                self.url=url    
        def get_html(self):
                page_req=requests.get(self.url)
                temp_html=page_req.text
		return temp_html

class GIF():
	def __init__(self,url,see_lz):
		self.URL=url
		self.SEE_LZ=see_lz
	def get_page_sum():
		pass

#baseurl='http://tieba.baidu.com/p/2858210485'
baseurl='http://tieba.baidu.com/p/3949977663'
####是否只看LZ
see_lz='0'
###初始页码
pg_no=1

#####获取页码总数
page_count=re.compile(r'<li class.*共.*</li>')
page_count_num=re.compile(r'\d{1,}')
####获取gif正则表达式模式
#gif_section_pattern=re.compile(r'<img class="BDE_Image".*?>')
###09-09修改正则表达式模式，只抓取gif文件
#gif_section_pattern=re.compile(r'<img class="BDE_Image".*?pic_ext="gif"\s*>')
gif_section_pattern=re.compile(r'<img class="BDE_Image".*?pic_ext="gif"')


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
	#request=urllib2.Request(url)
	#response=urllib2.urlopen(request)
	#page=response.read()
	page=HTML(url).get_html()
	
	gif_section=gif_section_pattern.findall(page)
	####当前页面gif总数
	gif_count=gif_section.__len__()
	print "当前页面gif总数为",gif_section.__len__(),"个"
	
	####当前页面上gif地址列表
	url_list=map(useful_functions.get_url_from_html,gif_section)	
	count=1
	for i in url_list:
		base_dir='/tmp/gif_save/'
		###获取gif文件名
		file_name=i.split('/')[-1].split('.')[0]	
		gif_save_path=base_dir+file_name+".gif"
		####user_list中的i就是url地址
		print "正在下载第",count,"张gif~~~~"
		####2015-09-11 修改gif的下载方式为request+file操作,urllib.retrieve方法不稳定
		####linux下测试通过
		gif_req=requests.get(i)
		with open(gif_save_path,'wb') as temp_file:
			for temp_chunk in gif_req.iter_content(chunk_size=1024):
				temp_file.write(temp_chunk)
		####修改gif下载的方式，改由request库+fileobject写文件的方式进行
		###urlretrieve下载方法在windows下测试通过
		#urllib.urlretrieve(i,gif_save_path)
#		time.sleep(2)
		count+=1	
	pg_no=pg_no+1
	if pg_no >1:#####测试,仅处理第一页，后续删掉这一行
	#if pg_no >page_count:
		print "全部页面下载完成，退出"
		break
	else:
		###不需要键盘干预，程序自动执行
		continue
