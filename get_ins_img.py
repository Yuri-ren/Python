#coding: utf-8

'''
下载instgram上的图片，选取最大分辨率的来下载
'''
from bs4 import BeautifulSoup
import requests
import os
import re
import random


def grap_img1():
    url_pattern=re.compile(r'\"display_resources":\[\{\"src\".*?]')
    img_pattern=re.compile(r'\[.*\]$')
    img_url_pattern=re.compile(r'http[s]?:[^\"]+')

    ins_url="https://www.instagram.com/p/B4zoD0AhqGi/?igshid=3b9f07ptlkw4"
    soup=BeautifulSoup(requests.get(ins_url).text,"html.parser")
    #print(soup.prettify)
    #print(soup.script)
    #os._exit(-1)
    for meta in soup.find_all("script",type="text/javascript"):
        #print(meta.string)
        ##取出特定属性的tag之后再对其string进行正则匹配
        ##string不为空的再转为byte进行比较
        if meta.string:
            #print(meta.string.encode('utf-8'))
            re_string=str(meta.string.strip().encode('utf-8'))
            #print(type(re_string))
            #print(re_string)
            #print(re.search(url_pattern,re_string))
            if(re.search(url_pattern,re_string)):
                ##已经匹配到包含img url的string了
                ##使用re.group()来抓取已经匹配上的字符串部分
                ##url中\u0026表示&符号，要再作一次转换才行
                temp_re_secton=re.search(url_pattern,re_string).group().replace(r'\\u0026','&').replace(r'"display_resources":','').replace('[','').replace(']','')
                ##直接取出url来
                #print(re.findall(img_url_pattern,temp_re_secton))
                ##取出来URL，对应的去请求header，然后根据response header中的content-length来判断文件大小
                #res_dist={'final_url':'','img_size':0}
                init_img_size=0
                #print(type(init_img_size))
                for i in re.findall(img_url_pattern,temp_re_secton):
                    temp_req=requests.get(i)
                    temp_file_size=int(temp_req.headers['content-length'])
                    if temp_file_size>init_img_size:
                        init_img_size=temp_file_size
                        download_url=i
                        return download_url

def get_img(url: object) -> object:
    ##存匹配文件名的路径临时list
    img_dir='/Users/bayudan/Desktop/'
    tmp_path_list=[]
    ##通过url取得的文件名
    file_type = url.split('?')[0].split('/')[-1]
    ##随机生成文件名
    file_name = ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd', 'c', 'b', 'a'], 5))
    file_path = img_dir + file_name + file_type
    print(file_path)
    img_req = requests.get(url)
    with open(file_path, 'wb') as fileh:
        fileh.write(img_req.content)

img=grap_img1()
print(img)
get_img(img)
