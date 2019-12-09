# coding: utf-8

'''
登陆91flac的测试脚本
add by yuri
'''
import requests
from bs4 import BeautifulSoup
import os,sys
##login url:https://www.91flac.com/login
##then 302 location https://www.91flac.com/users/vip

yuri_password=sys.argv[1]


fake_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Referer': 'https://www.91flac.com/login'
}


s=requests.Session()
login_req=s.get('https://www.91flac.com/login')
##页面正常响应的话，获取login页面中的csrf-token值
if login_req.status_code==200:
    soup=BeautifulSoup(login_req.text,'html.parser')
    ##找到页面中csrf这一段
    temp_res=soup.head.find(attrs={'name':'csrf-token'})
    ##取出csrf的值
    if temp_res:
        page_token=temp_res['content']
else:
    print("页面响应异常")
    os._exit(-1)

##携带上一步取到的csrf值以及对应的用户名密码，post数据即可登陆
login_post_data={'_token':page_token,'email':'79052441@qq.com','password':yuri_password,'remember':'on'}
print(login_post_data)
token_log_req=s.post('https://www.91flac.com/login',data=login_post_data,headers=fake_headers)
print(token_log_req.status_code)
print(token_log_req.cookies['XSRF-TOKEN'])
print(s.get('https://www.91flac.com/users/histories/audio').text)
print(s.get('https://www.91flac.com/users/histories/audio').cookies['XSRF-TOKEN'])
##至此，成功登录。
