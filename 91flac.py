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

##login post data(parameters)
#_token: VvW2mmhmDIYW4RetyX3bWiPFV6PZm8dmO7bJFyl5
#email: 79052441%40qq.com

yuri_password=sys.argv[1]
##
#Cookie: XSRF-TOKEN=eyJpdiI6IjlnV1pDUDJHXC93MFwvTlwvR1FjR0VqTHc9PSIsInZhbHVlIjoiWmxnXC96aUFUaEZCZHFrXC80SW5mQjZMNEU4bDFlNTdBZlo1MlRUZzB1dTBVdE55YUJKRGkxcnRCd0JQNGxsemh6IiwibWFjIjoiYmI5ZWNlODgyMTVkNTIwMzY5NzE2MmQzMWNlYmViNzQ5YTExZGRmNzZlODZkYTM0OTYwNjQ5ZDAyMTlmN2Q1ZiJ9; 91flac_session=eyJpdiI6Im45RnpkTTYzdW1zYnNlWnN5c2tUWlE9PSIsInZhbHVlIjoiTG41UnRZbHBhQlB0KzhJcVlWUmpxVzVLWU5CQ3A5WGUxeFdjdzBTUlZueldVTnZEd0l0YytHWVA2ejN4TXJzaiIsIm1hYyI6ImFhMzgxODgzYjM4NzlkZjM5ZWZkYTA0ODkwN2UwNGU4ZTA3NmU3ZDhjNjQ0OGVjM2JlNzdlNzZkMzM0ZjlkNzkifQ%3D%3D; _ga=GA1.2.1359275072.1566025163; _gid=GA1.2.1386488556.1566025163; _gat_gtag_UA_118813886_1=1; Hm_lvt_af518ab1fe8f21a70e3f6d2cdceb85c4=1566025163; Hm_lpvt_af518ab1fe8f21a70e3f6d2cdceb85c4=1566025163

login_url='https://www.91flac.com/login'
fake_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Referer': 'https://www.91flac.com/login'
}

login_post_data={'_token':'VvW2mmhmDIYW4RetyX3bWiPFV6PZm8dmO7bJFyl5','email':'79052441@qq.com','password':yuri_password,'remember':'on'}




def get_fake_headers():
    ##首先随便请求首页，获得response中的XSRF-TOKEN以及91flac_session两个token
    first_cookie=requests.get('https://www.91flac.com/',headers=fake_headers).cookies
    print(first_cookie['XSRF-TOKEN'])
    log_req=requests.get('https://www.91flac.com/login',headers=fake_headers,cookies=first_cookie)
    print(log_req.status_code)
    print(log_req.cookies)


s=requests.Session()
login_req=s.get('https://www.91flac.com/login')
##页面正常响应的话，获取login页面中的csrf-token值
if login_req.status_code==200:
    soup=BeautifulSoup(login_req.text,'html.parser')
    ##找到页面中csrf这一段
    temp_res=soup.head.find(attrs={'name':'csrf-token'})
    ##取出csrf的值
    if temp_res:
        page_csrf=temp_res['content']
else:
    print("页面响应异常")
    os._exit(-1)
print(page_csrf)
os._exit(-2)
temp_tag=soup.head.find_all('meta')
for i in temp_tag:
    #print(type(i))
    temp_dict=i.attrs
    #print(i.attrs)
    for key in temp_dict:
        #print(key)
        if temp_dict[key] == 'csrf-token':
            page_token=temp_dict['content']



login_post_data={'_token':page_token,'email':'79052441@qq.com','password':yuri_password,'remember':'on'}
print(login_post_data)
token_log_req=s.post('https://www.91flac.com/login',data=login_post_data,headers=fake_headers)
print(token_log_req.status_code)
#print(token_log_req.text)
print(token_log_req.cookies['XSRF-TOKEN'])
#print(s.get('https://www.91flac.com/users/histories/audio').text)
print(s.get('https://www.91flac.com/users/histories/audio').cookies['XSRF-TOKEN'])
##至此，成功登录。
