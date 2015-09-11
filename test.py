import re
import urllib
import requests

#req=requests.request('get','http://www.sh.com')
#print req.text
req=requests.get('http://imgsrc.baidu.com/forum/w%3D580/sign=2550bd7a5a82b2b7a79f39cc01adcb0a/a908acaf2edda3ccf8cd9d5e02e93901213f9265.jpg')
with open('/tmp/test.gif','w') as file_temp:
	for chunk in req.iter_content(chunk_size=1024):
		file_temp.write(chunk)
#with open('/tmp/test.log','w') as file:
#	file.write('hello\nhello,ren')
