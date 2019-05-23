import pymysql

# 1. 连接数据库
# host 主机名 可以是ip
# user 数据库的用户名
# password 密码
# db 数据库
# port  端口号，默认是3306
# charset  字符集
conn = pymysql.Connect(host='10.0.128.217',user='root',
                       password='123',db='test',port=3306,charset='utf8')

# print(conn)
# 2 创建游标
cursor = conn.cursor()
# print(cursor)

# 3 执行sql
sql = "select sno,sname from student"
# 返回值是受影响行数
res = cursor.execute(sql)
# print(res)
if res > 0:
    # 4 获取数据
    # 获取一条记录
    # record = cursor.fetchone()
    # print(record)
    # record = cursor.fetchone()
    # print(record)
    # record = cursor.fetchone()
    # print(record)
    # record = cursor.fetchone()
    # print(record)
    # record = cursor.fetchone()
    # print(record)
    # record = cursor.fetchone()
    # print(record)
    # record = cursor.fetchone()
    # print(record)
    # while 1:
    #     record = cursor.fetchone()
    #     if record == None:
    #         break
    #     print(record)
    # 取多条记录
    # records = cursor.fetchmany(1000)
    # print(records)
    # 获取所有记录
    records = cursor.fetchall()
    print(records)


# 5 关闭连接和游标
cursor.close()
conn.close()