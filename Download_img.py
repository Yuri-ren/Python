# -*- coding:utf-8 -*-
import re
import urllib
import urllib2

temp_url="http://tieba.baidu.com/p/3196294113?pn="
page=1
url=temp_url+'1'

response=urllib.urlopen(url)

#print response.getcode()
html=response.read()
