# -*- coding: utf-8 -*-
import re
import os
import requests
import json
import urllib2
import urllib
import rsa
import base64
import binascii
import cookielib

###Base64编码用户名
def get_su(user_name):
    username_ = urllib.quote(user_name)     # html字符转义
    username = base64.encodestring(username_)[:-1]
    return username

###得到servertime nonce pubkey rsakv
req_url='http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=MTg2NjE2MzY5Mjc%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1445587028278'
req=requests.get(req_url)
return_dict=eval(re.search(r'{.*}',req.content).group())

servertime=return_dict.get('servertime')
nonce=return_dict.get('nonce')
rsakv=return_dict.get('rsakv')
pubkey=return_dict.get('pubkey')
passwd='youyin676890'

###由servertime nonce passwd使用rsa算法加密用户明文密码
def get_sp_rsa(passwd, servertime, nonce):
    # 这个值可以在prelogin得到,因为是固定值,所以写死在这里
    weibo_rsa_n=pubkey 
    weibo_rsa_e = 65537  # 10001对应的10进制
    message = str(servertime) + '\t' + str(nonce) + '\n' + passwd
    key = rsa.PublicKey(int(weibo_rsa_n, 16), weibo_rsa_e)
    encropy_pwd = rsa.encrypt(message, key)
    return binascii.b2a_hex(encropy_pwd)
sp=get_sp_rsa(passwd,servertime,nonce)

###构造POS参数,并请求http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)
post_data={'entry':'weibo','gateway':'1','from':'','savestate':'7','userticket':'1','pagerefer':'http://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=http%3A%2F%2Fweibo.com%2F&domain=.weibo.com&ua=php-sso_sdk_client-0.6.14&_rand=1445590178.9717','vsnf':'1','su':'MTg2NjE2MzY5Mjc=','server':'miniblog','servertime':servertime,'nonce':nonce,'pwencode':'rsa2','rsakv':rsakv,'sp':sp,'encoding': 'UTF-8','url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack','returntype':'META'}
#print type(post_data)

login_req_url='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
req_login=requests.post(login_req_url,data=post_data)
cookie_content=req_login.content

####取得cookie的URL
cookie_url= re.findall(r'http://.*\'',cookie_content)[0].split('\'')[0]
#print cookie_url


###保存cookie
cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
response=opener.open(cookie_url)
for i in cookie:
	print i.name
#	print i.value
test_login_url='http://weibo.com/1912727485/follow?rightmod=1&wvr=6'
test_req=requests.get(test_login_url,cookies=cookie)
#print test_req.content

