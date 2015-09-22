#coding:utf-8
import re
import urllib
import requests
import sys
import useful_functions

####根据URL获取网页源代码的class
class HTML():
	def __init__(self,url):
		self.url=url	
	def get_html(self):
		page_req=requests.get(self.url)
		return page_req.text

class GIF():
        def __init__(self,base_url,see_lz,begin_page):
                self.URL=base_url
                self.SEE_LZ=see_lz
		self.BEGIN_PAGE=begin_page
		#self.HTML_PAGE=HTML('self.URL').get_html()
		#print type(self.HTML_PAGE)
	def join_url(self):
		#current_url=
		pass
        def get_page_sum(self):
		###获取页码总数的正则表达式
		page_count=re.compile(r'<li class.*共.*</li>')
		page_count_num=re.compile(r'\d{1,}')	
		page_html=str(HTML(self.URL).get_html().encode('utf-8'))
		print type(page_html)	
		temp_page_count=page_count.findall(page_html)[0]
		temp_page_count_1=useful_functions.del_tag(temp_page_count).split('，')[-1]
		####页码总数
		page_count=int(page_count_num.findall(temp_page_count_1)[0])
		return page_count

	def get_url(self):
		pass
		#print type
		#print self.URL
		#print self.SEE_LZ
test=GIF('http://tieba.baidu.com/p/3402566773',0,1)
test.get_page_sum()
#yemian=HTML('http://tieba.baidu.com/p/3402566773')
#temp=yemian.get_html()
#print type(temp)
