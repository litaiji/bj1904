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
sql = """
create table  if not exists user(uid int primary key auto_increment,username varchar(30) not null,password char(48) not null);
"""

# 返回值是受影响行数
res = cursor.execute(sql)




# 5 关闭连接和游标
cursor.close()
conn.close()