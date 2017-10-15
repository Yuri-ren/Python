#coding: utf-8

import poplib
'''
获取最新的邮件内容
将上次读取的最新邮件编号持久化保存下来 每次拿到最新的mail list后 取出这一段的内容 并在其中过滤下邮件的Subject进行处理
'''

user_name='renyouyin'
user_passwd=''
mail_server='mail.xunlei.com'

p=poplib.POP3(mail_server,port=110)
##deal with login exception
try:
    p.user(user_name)
    p.pass_(user_passwd)
except :
    print u'登陆邮箱失败!'
else:
    #print p.getwelcome()
    ##login success
    print u"登陆邮箱成功~"
    mail_count=p.stat()[0]
    print mail_count
    ##list显示所有邮件的编号
    #print p.list()

    p.quit()
