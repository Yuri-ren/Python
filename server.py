# -*- coding: utf-8 -*-
import socket
import time
import threading
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(3)
while True:
	sock,addr=s.accept()
	print "Connected by ",addr
	client_data=sock.recv(1024)
	return_data=os.popen(client_data).read()
	#print type(return_data)
	sock.send(return_data)
	sock.close()
s.close()
