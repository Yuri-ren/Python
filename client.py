# -*- coding: utf-8 -*-
import socket
import time
import threading
import os

#print socket.gethostbyname('www.sh.com')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
s.send("ls -l")
#while True:
#	temp_data=s.recv(1024)
#	if temp_data=='':
#		break
#	print temp_data
print s.recv(2048)
s.close()
