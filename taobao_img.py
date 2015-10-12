# -*- coding: utf-8 -*-
import re
import requests
import json
import os


########淘宝页面商品详情为js动态加载，所以python抓取静态页面的方法无法获取到图片地址，采用直接抓取js地址，然后对其进行请求，得到json字符串，得到图片文件名
__author__='Yuri'

####淘宝图片地址，后续进行图片地址拼接
img_server='http://img.alicdn.com/imgextra/'

###re pattern 
js_pattern=re.compile(r'apiImgInfo:"//otds.alicdn.com/json/item_imgs.htm.*?"')
seller_pattern=re.compile(r'.sellerId:".*?"')
js2dict_pattern=re.compile(r'{.*}',re.S)
filetype_pattern=re.compile(r'.*\..*')

####get html page
####根据系统,windows|linux来显示提示字符,防止乱码
platform=os.name
if(platform=='nt'):
	base_url=raw_input(u'请输入要下载的页面地址:'.encode('gbk'))
else:
	base_url=raw_input('请输入要下载的页面地址:')

os._exit(-1)
req=requests.get('base_url')
html_page=req.text

#####获取卖家ID
temp_seller=seller_pattern.findall(html_page)
seller_id=str(temp_seller[0].split('"')[-2])

js_temp=js_pattern.findall(html_page)
####得到生成图片的js地址
img_js=str(js_temp[0].split('"')[-2].split('//')[-1])
img_js_url="http://"+img_js

###请求该js地址，获得关于图片地址json字符串
js_req=requests.get(img_js_url)
temp_json=js_req.text

#####将unicode字符转换为utf编码
def u2utf8(temp_string):
	return temp_string.encode('utf8')

###将json字符串转换为字典
js_dict=js2dict_pattern.findall(temp_json)[0]
img_url_dict=json.loads(js_dict)

####temp_img_list为暂存图片文件名的列表
temp_img_list=[]
for i in img_url_dict.keys():
	temp_item=u2utf8(i)
	if filetype_pattern.search(temp_item) is None:
		continue
	else:
		temp_img_list.append(temp_item)
		
###map函数，拼接完整的图片文件URL地址
def url_map(temp_url):
	img_url=img_server+temp_url	
	return img_url

img_url=map(url_map,temp_img_list)
img_num=len(img_url)
print img_url
os._exit(0)
####下载图片文件
img_count=1
print "当前页面商品图片总数为",img_num
for i in img_url:
	###获取文件名
	img_name=i.split('/')[-1]
	img_dir='/tmp/taobao_img/'
	img_path=img_dir+img_name
	print "正在下载第",img_count,"张图片"
	img_req=requests.get(i)
	with open(img_path,'wb') as temp_file:
		for temp_chunk in img_req.iter_content(chunk_size=1024):
			temp_file.write(temp_chunk)
	img_count+=1
	if (img_count>img_num):
		print "下载完成，退出~~"
		break
	else:
		continue











