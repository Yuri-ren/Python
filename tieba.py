# -*- coding:utf-8 -*-
import re
import string 
import urllib2
import urllib

url='http://tieba.baidu.com/p/3138733512?'
post_data={'pn':1,'see_lz':'1'}
#post_data=[('see_lz',1),('pn',1)]
data=urllib.urlencode(post_data)

#request=urllib2.Request()
print data
response=urllib.urlopen(url,data)
print response.geturl()
#print response.read()
