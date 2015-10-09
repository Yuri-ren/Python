# -*- coding: utf-8 -*-
import socket
import time
import threading
import os

#####清空ip记录的脚本
delete_log="sed -i '1,$'d /tmp/iptables-test.log"

####服务器端启动线程来处理来自client端的信息
def proc(sock,addr):
	print "Accept connection from %s:%s...." %addr
	sock.send("Now Server will add IPs to the iptables according to your input~~~~")
	os.system(delete_log)
	while True:
		data=sock.recv(1024)
		if data == 'exit' or not data:
			break
		with open ('/tmp/iptables-test.log','a') as temp_file:
			temp_file.write(data+'\n')
		#print data
		sock.send("Return"+str(data))
	sock.close()
	print "Connection from %s:%s has been closed.....waitting for next connection" %addr

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9888))
s.listen(5)

while True:
	sock,addr=s.accept()
	print "链接来自client %s:%s:" %addr
	t=threading.Thread(target=proc,args=(sock,addr))
	t.start()
