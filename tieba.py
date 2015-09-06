# -*- coding:utf-8 -*-
import re
import string 
import urllib2
import urllib

class BDTB:
	#baseURL=''
	#see_lz=''
	###类的初始化方法
	def __init__(self,baseurl,seelz):
		self.baseURL=baseurl
		self.see_lz='?see_lz='+str(seelz)
	def get_page(self,pageNum):
		url=self.baseURL+self.see_lz+'&pn='+str(pageNum)
		request=urllib2.Request(url)
		response=urllib2.urlopen(request)
		return response.read()
	def print_url(self):
		print self.baseURL
		print self.see_lz

url='http://tieba.baidu.com/p/3196294113'
bdtb=BDTB(url,1)
temp_page=bdtb.get_page(1)
print type(temp_page)
#print temp_page
