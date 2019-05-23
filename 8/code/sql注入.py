import hashlib

import pymysql
import settings

# 1. 连接数据库
# host 主机名 可以是ip
# user 数据库的用户名
# password 密码
# db 数据库
# port  端口号，默认是3306
# charset  字符集
# conn = pymysql.Connect(host='10.0.128.217',user='root',
#                        password='123',db='test',port=3306,charset='utf8')
conn = pymysql.Connect(**settings.parameters)


# print(conn)
# 2 创建游标
# 默认返回的数据格式： （（），（））
# cursor=pymysql.cursors.DictCursor 返回的格式：[{'sno': '101', 'sname': '李军'},{}]
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# print(cursor)

# 3 执行sql
username = input("请输入用户名：")
password = input("请输入密码：")
password = hashlib.sha1(password.encode('utf8')).hexdigest()
print(password)
# 请输入用户名：kkkd' or 1 or '1
# 请输入密码：ddd
#
# sql = "select username,password from user where username='%s' and password='%s'" % (username,password)

#  防止注入
# 将输入中特殊字符转义
# username = pymysql.escape_string(username)
# print(username)
# sql = "select username,password from user where username='%s' and password='%s'" % (username,password)
sql = "select username,password from user where username=%s and password=%s"
print(sql)
# 返回值是受影响行数
#  第一个参数是sql语句
# 第二个参数是sql语句带的参数,可以防止注入攻击
res = cursor.execute(sql,[username,password])
# print(res)
if res > 0:
    print("登录成功")
else:
    print("登录失败")


# 5 关闭连接和游标
cursor.close()
conn.close()