# -*- coding: utf-8 -*-
import re
import string
import urllib2
import requests

####http request headers
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36','refer':'https://dadalatte.taobao.com/category-683023208.htm?spm=a1z10.5-c.w4010-1622594244.43.sthwwj&search=y&parentCatId=659549153&parentCatName=2013+NEW+ARRIVAL++%26gt%3B%26gt%3B&catName=03%D4%C210%C8%D5%C9%CF%D0%C2'}


__author__='Yuri'
###re pattern 
desc_pattern=re.compile(r'<div id="description" class="tshop-psm ke-post J_DetailSection">.*?</div>',re.S)
req=requests.get('https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-1622594245.20.LSHO4C&id=23034096541',headers=headers)

html_page=req.text
print html_page
temp_sector=desc_pattern.findall(html_page)
print len(temp_sector)
for i in temp_sector:
	print i
