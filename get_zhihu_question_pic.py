# -*- coding: utf-8 -*-
import requests
import re
import random,os
import json
from PIL import Image
# pip install Pillow


##def http requests headers
my_headers={
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    'Host': "www.zhihu.com",
    'Origin': "http://www.zhihu.com/",
    'Pragma': "no-cache",
    'Referer': "http://www.zhihu.com/",
    'X-Requested-With': "XMLHttpRequest"
}

def test():
    req=requests.get('https://www.zhihu.com',headers=my_headers)
    print req.text

###构造Session对象，用于验证码校验以及全局requests
s=requests.Session()

###重新写获取验证码的函数
def get_verify_code():
    url="https://www.zhihu.com/captcha.gif?r=1496212778758&type=login&lang=en"
    req=s.get(url,headers=my_headers)
    with open ('/tmp/verify.gif','wb') as temp_file:
        for temp_chunk in req.iter_content(chunk_size=1024):
            temp_file.write(temp_chunk)
    ###打开验证码图片手动输入
    im=Image.open('/tmp/verify.gif')
    ##显示图片
    im.show()
    verify_code=raw_input("input the verify code you have seen in your browser:")
    return verify_code


##通过随便请求一个页面来获得cookie,并且读取cookie来取得xsrf;此处应该使用session来做
def get_xsrf():
    req=s.get('https://www.zhihu.com',headers=my_headers)
    return req.cookies.get('_xsrf')

###构造post data并模拟登陆知乎 使用手机号码登录
def login_zhihu():
    login_url='https://www.zhihu.com/login/phone_num'
    form={}

    ####构造form 表单
    form['_xsrf']=get_xsrf()
    form['remember_me']='true'
    form['phone_num']='18576785181'
    form['password']='15854784557'
    form['captcha_type']='en'
    form['captcha']=get_verify_code()

    ####请求登陆URL
    req=s.post(login_url,headers=my_headers,data=form)
    ####返回的消息格式，为字典类型，dict['msg','r'],msg为消息内容，r为返回码
    return_dict=req.json()
    #print return_dict
    if(return_dict['r']==0):
	print u"登陆成功~"
    else:
        print u"登陆失败!!!"
	print u"失败原因:",return_dict['msg']
	os._exit(-2)

if __name__=="__main__":
    login_zhihu()
