#coding: utf-8

import requests
import bs4
import os
import cPickle as pickle
import sys

#print sys.path
#sys.path.append('/usr/local/python2.7.5/lib/python2.7/site-packages/bs4/')
#print sys.path

##先取得上一次保存的最新活动
old_act_list=pickle.load(open("/home/root1/last_act_list",'r'))

###获取活动的真正网址
def get_real_url(title,url):
	real_title=title
	real_url=''
	req=requests.get(url)
	req.encoding='utf-8'
        temp_soup=req.text
	soup=bs4.BeautifulSoup(temp_soup,"html.parser")
	tag=soup.article.find_all('a')
	for i in tag:
		temp_url=i['href']
		if 'cf.qq.com' in temp_url:
			real_url=temp_url
	return real_title,real_url

#print get_real_url('CF王牌幸运星2月网址 幸运折扣抽奖 C哥抽到1折','http://www.cfhuodong.com/2017-2-21.html')
#os._exit(-1)

###获取cf最新活动
def get_cf_act():
	#res_dict={'title':'','url':''}
	res_list=[]
	url='http://www.cfhuodong.com/zuixin/'
	req=requests.get(url)
	req.encoding='utf-8'
	temp_soup=req.text

	soup=bs4.BeautifulSoup(temp_soup,"html.parser")
	tag=soup.article.find_all('p')
	for s in soup.find_all('article'):
		res_dict={'title':'','url':''}
		##s为单独的活动大段
		###get the url
		act_url=s.a['href'].encode('utf-8')
		act_title=unicode(s.a.string)
		res_dict['title']=act_title
		res_dict['url']=act_url
		#print json.dumps(res_dict, encoding="UTF-8", ensure_ascii=False)
		res_list.append(res_dict)
	return res_list
	
temp_act_list=get_cf_act()
###将结果持久化保存
with open('/home/root1/last_act_list','w') as f:
    f.write(pickle.dumps(temp_act_list))
#print temp_list

##compare result with old_act_list
cmp_res=cmp(old_act_list,temp_act_list)
if cmp_res==0:
	print "无最新活动~"
else:
	##首页活动有变化 抓取最新活动
	for i in temp_act_list:
		if i not in old_act_list:
			##最新活动
			#print i['title'],i['url']
			fin_title,fin_url=get_real_url(i['title'],i['url'])
			#wechat msg
			#msg="最新活动:",fin_title,"URL为:",fin_url
			msg=fin_title+fin_url
			print msg
			##send weichat message
			push_dict={'to':'renyouyin','msg':'','sub':'jiankong','method':'wx'}
			push_dict['msg']=msg
			req=requests.post("http://alarm.cc.p2cdn.com:8080/alarm",data=push_dict)
