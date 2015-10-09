# -*- coding: utf-8 -*-
import socket
import re

######通过socket连接服务器并添加IP到防火墙

server_ip=''
ip_list=[]
	
#####regular pattern
ip_format_pattern=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

#def string2list(str):
#	input_list=str.split(',')
#	return input_list

input_server_ip=raw_input("服务器端IP:")
try:
	ip_format



input_str=raw_input("IPs,splited by ','>")
input_list=string2list(input_str)
print input_list

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9888))
# 接收欢迎消息:
print s.recv(1024)

for data in input_list:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
