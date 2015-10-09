#coding:utf-8
import re
import urllib
import requests
import urllib2
import socks
import socket

###http headers
test_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
test_header1={'User-Agent':'renyouyin-test'}
test_header2={'User-Agent':'wspoll-renyouyin'}

######HTTP Proxy
http_proxy={'https':'https://101.254.140.170:80','http':'http://101.254.140.170:80'}

######Sock Proxy
sock_proxy={'http':'socks5://203.195.140.67:1080/'}


socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "203.195.140.67",1080)
socket.socket = socks.socksocket

####requests不支持sock代理方式
#req_2=requests.get('http://www.sh.com/',proxies=sock_proxy)
#print req_2.status_code

#req=urllib2.request('http://www.sh.com/',)
response=urllib2.urlopen('http://www.sh.com/')
print response.getcode()
