# -*- coding: utf-8 -*-
import requests
import re
import random,os
import json

###构造Session对象，用于验证码校验以及全局requests
s=requests.Session()

###获取验证码的函数
def get_verify_code():
	url='http://www.zhihu.com/captcha.gif'
	
	req=s.get(url,params={'r':random.random()})
	#####保存验证码图片
	with open ('verify.gif','wb') as temp_file:
		for temp_chunk in req.iter_content(chunk_size=1024):
			temp_file.write(temp_chunk)
	####打开外部浏览器渲染验证码并手工输入,直接使用os.system()打开
	os.system('verify.gif')
	verify_code=raw_input("input the verify code you have seen in your browser:")
	return verify_code

###获取知乎页面xsrf值的函数
def get_xsrf():
	req=requests.get('http://www.zhihu.com')
	html_page=req.content
	xsrf=re.search(r'<input type=\"hidden\" name=\"_xsrf\" value=\".*\"',html_page).group().split('"')[-2]
	return xsrf

###构造post data并模拟登陆知乎
def login_zhihu(account,password):
	form={}
	####区分email账户与手机号
	if(re.search(r'\w*@\w*\.\w*',account)):
		print "email account~"
		login_url='http://www.zhihu.com/login/email'
	elif(re.search(r'\d{11}',account)):
		print "mobile_phone account~"
		login_url='http://www.zhihu.com/login/phone_num'
	else:
		print "Account type error!!!"

	####构造http request header	
	headers = {
    	'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
        'Host': "www.zhihu.com",
        'Origin': "http://www.zhihu.com/",
        'Pragma': "no-cache",
        'Referer': "http://www.zhihu.com/",
        'X-Requested-With': "XMLHttpRequest"
    }

    ####构造form 表单
	form['_xsrf']=get_xsrf()
	form['remember_me']='true'
	form['email']=account
	form['password']=password
	form['captcha']=get_verify_code()

    ####请求登陆URL
	req=s.post(login_url,headers=headers,data=form)
	####返回的消息格式，为字典类型，dict['msg','r'],msg为消息内容，r为返回码
	return_dict=req.json()
	if(return_dict['r']==0):
		print u"登陆成功~"
	else:
		print u"登陆失败!!!"
		print u"失败原因:",return_dict['msg']
		os._exit(-2)
	#test_req=s.get('http://www.zhihu.com/people/ren-you-yin/topics')
	#print test_req.content

###测试代码
if __name__=='__main__':
	#print get_xsrf()
	#get_verify_code()6rrl
	#login_zhihu('18661636927','')
	account=raw_input("input your Zhihu account:")
	password=raw_input("input your account password:")
	login_zhihu(account,password)
else:
	pass
