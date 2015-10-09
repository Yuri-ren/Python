# -*- coding: utf-8 -*-
import socket
import re
import os

######通过socket连接服务器并添加IP到防火墙
__author__='renyouyin'


####server_ip为要操作的服务器IP，ip_list为需要添加到防火墙的公网IP
server_ip=''
ip_list=[]
	
#####regular pattern
ip_format_pattern=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

#while False:
while True:
	try:
		input_server_ip=raw_input(u"请输入服务器端IP:".encode('gbk'))
		if ip_format_pattern.search(input_server_ip) is None:
			raise ValueError
	except ValueError:
		print u"输入的IP格式有误,请重新输入！".encode('gbk')
	except KeyboardInterrupt:
		print u"\n退出ing.....".encode('gbk')
	else:
		server_ip=input_server_ip
		break


input_str=raw_input(u"输入要添加到防火墙例外的IP,多个IP地址的话以逗号分隔:".encode('gbk'))

input_list=input_str.split(',')
#print input_list
for i in input_list:
	if ip_format_pattern.search(i) is None:
		print i,u"格式有误!!".encode('gbk')
		os._exit(0)
	else:
		ip_list.append(i)

#print ip_list

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect((server_ip, 9888))
# 接收欢迎消息:
print s.recv(1024)

for data in input_list:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
