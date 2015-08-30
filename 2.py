# -*- coding:utf-8 -*-
__author__='Yuri'
import re
import urllib2
import urllib

page=21
url='http://www.qiushibaike.com/hot/page/'+str(page)
######抓取段子内容###
content_pattern=re.compile(r'<div class="content".*?</div>',re.S)
#######过滤图片和视频###
filter_pattern=re.compile(r'<div class="thumb">|<video class')
####从页面中抓取作者
author_pattern=re.compile(r'<div class="author">.*?</div>',re.S)
real_author_pattern=re.compile(r'<.*>')
#####08-26抓取网页中的作者和段子部分
author_duanzi_pattern=re.compile(r'<div class="author">.*<div class="content">.*?</div>',re.S)
#####过滤匿名用户-08-27
anonymous_pattern=re.compile(r'<div class="author">',re.M)
<<<<<<< HEAD
#####过滤段子信息
duanzi_status_pattern=re.compile(r'<span class="stats-vote">.*?</span>',re.S)

###添加http请求头，防止网站屏蔽
user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
header={'User-Agent':user_agent}

####由html页面中取出author
def name_Func(str):
	pattern=re.compile(r'<.*?>')	
	list=pattern.findall(str)
	for i in list:
		str=str.replace(i,'')
	return str
def print_List_Func(list):
	for i in list:
		print i
		print '-'*20

def replace_Func(str):
    list1=[]
    list2=str.split('\n')
    for i in list2:
        if i=='':
            continue
        else:
            list1.append(i)
    return list1
######去除字符串里面的tag并取出点赞数目
def del_tag(str):
        pattern=re.compile(r'<.*?>')
        list=pattern.findall(str)
        for i in list:
                str=str.replace(i,'')
        return str.split(' ')[0]


####去除单个字符串里面的空格
def del_space_func(str):
	list=[]
	temp_list=str.split('\n')
	for i in temp_list:
		if i=='':
			continue
		else:
			list.append(i)
	new_str=list[0]
	return new_str


try:
	request=urllib2.Request(url,headers=header)
	response=urllib2.urlopen(request)
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason

html=response.read()

pattern=re.compile(r'<div class="article block untagged mb15".*?[\n]{6,}',re.S)
#pattern=re.compile(r'<div class="content">.*[^(<div class="article block untagged mb15")]*')
temp_list=pattern.findall(html)

#####08-26重写取作者和段子内容
for i in temp_list:
	final_list=[]
	author=''
	content=''
	vote=''
	if filter_pattern.search(i) is None:#####过滤段子内容是否含有图片或者视频
		if anonymous_pattern.search(i) is None:#####判断作者是否为匿名
			#print i,'\n','*'*10
			author='匿名用户'
			temp1_content=content_pattern.findall(i)[0]
			temp_content=name_Func(temp1_content)
			content=del_space_func(temp_content)
		else:
			a_d_temp=author_duanzi_pattern.findall(i)
			#print type(a_d_temp)
			#print a_d_temp.__len__()
			#for s in a_d_temp:
			#	print s
			temp_s=a_d_temp[0]
			temp_str=name_Func(temp_s)
			final_list=replace_Func(temp_str)
			author=final_list[0]
			content=final_list[1]
		temp_vote=duanzi_status_pattern.findall(i)
		vote=del_tag(temp_vote[0])
		print "作者:",author,'\t','点赞数:',vote
		print "作者:",author
		print content
		print '--'*40
	else:
		continue
