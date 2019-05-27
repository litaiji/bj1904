import re

from pymongo import MongoClient


# 连接mongo服务器
conn = MongoClient()

# 连接数据库
db = conn.bj1904


#  插入记录
db.user.insert({'name':'英拉','age':67,'sex':'女'})

# 返回的是可迭代对象
data = db.user.find({'name':re.compile('^川')})

data = list(data)
# for rec in data:
#     print(rec)
print(data)

# 关闭连接
conn.close()