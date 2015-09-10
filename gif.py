# -*- coding:utf-8 -*-
import re
import urllib2
import urllib
import useful_functions

__author__='Yuri'
#####下载百度贴吧url页面中的gif，自动遍历所有页面抓取
#####see_lz变量控制是否只看LZ

baseurl='http://tieba.baidu.com/p/3196294113'
#baseurl='http://tieba.baidu.com/p/3949977663'
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
gif_section_pattern=re.compile(r'<img class="BDE_Image".*?pic_ext="gif"\s*>')


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
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	page=response.read()
	
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
		urllib.urlretrieve(i,gif_save_path)
		count+=1	
	pg_no=pg_no+1
	#if pg_no >1:#####测试，后续删掉这一行
	if pg_no >page_count:
		print "全部页面下载完成，退出"
		break
	else:
		print "Enter键下载下一页,任意键退出......."
		input=raw_input()
        	if input is None or len(input) == 0:
			continue
		else:
			break




