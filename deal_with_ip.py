# -*- coding: utf-8 -*-
import requests
import sys,os
import re
import time
import sheng


command='rm -f ./deal_with_ip.code'

##清理之前记录文件
os.popen(command)

##通过阿里IP接口获取IP信息
def get_ip(ip):
        base_url="http://ip.taobao.com/service/getIpInfo.php?ip="
        url=base_url+str(ip)
        req=requests.get(url)
        res=req.json()['data']
        province=res['region'].encode('utf8')
        city=res['city'].encode('utf8')
        isp=res['isp'].encode('utf8')
        return province,city,isp


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
		pro,dict,yunyingshang=get_ip(ip1)
                ###host、ip1变量是最终要写入文件的变量
                code_result=sheng.get_code(pro,dict,yunyingshang)
                op1=str(code_result[0])
                pro1=str(code_result[1])
                dict1=str(code_result[2])
                #print host,ip1,op1,pro1,dict1
                ###最终结果写入文件,不写入文件也可以,重定向到文件保存
                file5=open('./deal_with_ip.code','a')
                file5.write(host+'\t'+ip1+'\t'+op1+'\t'+pro1+'\t'+dict1+'\n')
                file5.close()
		##防止请求过快被屏蔽
		time.sleep(3)
finally:
        fileh.close()
