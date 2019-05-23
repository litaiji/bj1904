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
# conn.select_db()

# print(conn)
# 2 创建游标
# 默认返回的数据格式： （（），（））
# cursor=pymysql.cursors.DictCursor 返回的格式：[{'sno': '101', 'sname': '李军'},{}]
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
print(cursor)

# 3 执行sql

username = input("请输入用户名：")
password = input("请输入密码：")

# 如果字段是字符串，请在字符串两边添加单引号
sql = """
insert into user(username,password) values ('%s',sha1('%s'))
""" % (username,password)
print(sql)
try:
    # pymysql默认开启事物
    # 插入成功返回1,否则返回0
    res = cursor.execute(sql)
    if res:
        conn.commit()
        # 获取新增加记录的自增主键值
        print(cursor.lastrowid)

        # 查看sql语句
        print(cursor._executed)
    else:
        conn.rollback()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    # 5 关闭连接和游标
    cursor.close()
    conn.close()



