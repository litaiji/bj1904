import redis

rd = redis.StrictRedis(host='10.0.128.162',password='123')
print(rd)

# 1 逐条命令执行
# rd.set('nameddd','路飞')
#
# # 返回值是字节流字符串
name = rd.get('name3333')
print(name)
# print(name.decode('utf8'))

# 2 批处理方式
# 管道会把多条命令打包执行，效率高
# pipe = rd.pipeline()
# pipe.set('a',20)
# pipe.set('b',30)
# pipe.set('c',40)
# pipe.execute()
