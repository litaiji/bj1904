import hashlib

import redis
import pymysql

from dbhelper import Dbhelper


rd = redis.StrictRedis()

username = input("请输入用户名")
password = input("请输入密码")
password = hashlib.sha1(password.encode('utf8')).hexdigest()
# 从redis查找用户名和密码
username1 =  rd.get('username_1').decode('utf8')
password1 = rd.get('password_1').decode('utf8')
print(username1,password1)

if username1 and username == username1:  # 用户名是否存在
    if password == password1:
        print("redis:登录成功")
    else:
        print("redis:登录失败,请重新登录")
else: # 到mysql中找
    db = Dbhelper('user')
    res = db.fields('uid').where(name=username,password=password).select()
    if res:
        print("mysql:登录成功")
        # 把数据写回redis
        rd.set('username_'+str(res[0]['uid']),username)
        rd.set('password_'+str(res[0]['uid']),password)
    else:
        print("mysql:登录失败,请重新登录")