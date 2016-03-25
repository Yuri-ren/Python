# -*- coding: utf-8 -*-
import requests
import sys,os
import re
import threading
import time
import sheng

command='rm -f ./deal_with_ip.code'
zhixiashi_list=['北京市','上海市','天津市','重庆市']
sheng_list=['云南省','台湾省','吉林省','四川省','安徽省','山东省','山西省','广东省','江苏省','江西省','河北省','河南省','浙江省','海南省','湖北省','湖南省','甘肃省','福建省','贵州省','辽宁省','陕西省','青海省','黑龙江省','西藏自治区','广西壮族自治区','新疆维吾尔自治区','宁夏回族自治区','内蒙古自治区','香港特别行政区','澳门特别行政区']

sec=re.compile(r'<table>.*<span class="c-gap-right">.*?</table>',re.S)
sec1=re.compile(r'IP地址.*[^\n]')

##清理之前记录文件
os.popen(command)

##通过百度获取IP归属地的函数
def deal_with_ip(ip):
        base_url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd='
        url=base_url+str(ip)
        req=requests.get(url)
        html=req.content
        temp_sec1=sec.search(html).group()
        temp_sec2=sec1.search(temp_sec1).group().rstrip()
        fina_info=re.split(r'<.*?>',temp_sec2)[-1]
        diqu=fina_info.split(' ')[-2].strip()
        yunying=fina_info.split(' ')[-1].strip()
        ###返回一个二元组(IP、地区、运营商)
        return diqu,yunying


#2.4版本不支持with open写法
#with open('./ip','r') as temp_file:
fileh=open('./deal_with_ip.list','r')
try:
        for i in fileh:
                ###分隔符号不一致的地方,为空格或者\t
                ###分割符号为空格
                if(' ' in i):
                        host,ip=i.split(' ')
                elif('  ' in i):
                        host,ip=i.split('       ')
                ip1=str(ip.strip('\n'))
                ###host、ip1变量是最终要写入文件的变量
                #t=threading.Thread(target=deal_with_ip,args=(ip1,))
                #t.start()
                ##同时请求数量过多的话，容易被封IP
                shengshi,yunyingshang=deal_with_ip(ip)
                if shengshi in zhixiashi_list:
                        ##直辖市以及只有省份信息的
                        pro_dict=shengshi+'\t'+'zhixiashi_null'
                else:
                        if shengshi in sheng_list:
                                pro_dict=shengshi+'\t'+'sheng_null'
                        else:
                                if('省' in shengshi):
                                        temp_str=shengshi.split('省')
                                        pro=temp_str[0]+'省'
                                        dict=temp_str[1]
                                        pro_dict=pro+'\t'+dict
                                else:
                                        if('区' in  shengshi):
                                                temp_str=shengshi.split('区')
                                                pro=temp_str[0]+'区'
                                                dict=temp_str[1]
                                                pro_dict=pro+'\t'+dict
                                        else:
                                                pro_dict="省市信息需要做特殊处理~~"
                code_result=sheng.get_code(pro,dict,yunyingshang)
                op1=str(code_result[0])
                pro1=str(code_result[1])
                dict1=str(code_result[2])
                #print host,ip1,op1,pro1,dict1
                ###最终结果写入文件,不写入文件也可以,重定向到文件保存
                file5=open('./deal_with_ip.code','a')
                file5.write(host+'\t'+ip1+'\t'+op1+'\t'+pro1+'\t'+dict1+'\n')
                file5.close()
finally:
        fileh.close()
