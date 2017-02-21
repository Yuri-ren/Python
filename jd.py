#coding: utf-8

import requests
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

login_url='https://passport.jd.com/uc/loginService?uuid=d4e5a306-2131-47c7-8803-212f99a1193f&ltype=logout&r=0.9748168177500238&version=2015'
req_header={
'Accept': "text/plain, */*; q=0.01",
'Accept-Encoding': "gzip, deflate, br",
'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
'Host': "passport.jd.com",
'Origin': "https://passport.jd.com",
'Refer': "https://passport.jd.com/uc/login?ltype=logout",
'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

send_data={
'uuid': "d4e5a306-2131-47c7-8803-212f99a1193f",
'eid': "5XOOZ7VGVZ7BQUEBGFA4W4F5SSTXRG2YCWSFBU5OZZRNJSY4XDX2T2N42EHHQVSRAHXR7STWFBPCU2FMO2JFFOWOC4",
'fp': "a5766da90be827355dd5a2a3abd2c237",
'_t': "_ntWPbhB",
'logintype': "f",
'loginname': "18661636927",
'nloginpwd': "X7UalO0ZfByb/uUZGcHU51g4IG5xy6KdiBQfQPDf2Zl3IsX0hWW3/6urLnPXIQ7/ErOlIxDbd4BVjrlb4nwjvbOyqVQbo8oqAAEL/BNqNgbe22gU1H2VyvJOT0NGoJW7rWxsTTQa730qVXPy8vpk0lJAOaGPJgWusb+RNTYxZEM=",
'chkRememberMe': "on",
'authcode': ""
}

s=requests.Session()
req=s.post(login_url,headers=req_header,data=send_data)
print type(req.text)

print req.status_code

#req_list=s.get("https://order.jd.com/center/list.action")
#print req_list.text
