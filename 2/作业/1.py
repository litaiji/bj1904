#1.统计一个字符串中出现频率最高的字符及其出现次数
import collections

# s1 = "sdjkfjksdkjfsfhjweuuiweuirsdjkfjksdfjhk"
# res = [(key,value)   for key,value in dict(collections.Counter(s1)).items()]
# # res.sort(key=lambda x:x[1],reverse=True)
# tmp = max(res,key=lambda x:x[1])
# print(tmp)
"""
2.自己实现一个find函数，功能和字符串find函数一模一样

- 比如传递 'i love you baby', 'love'   返回2
- 比如传递 'i love you baby', 'love1'  返回-1
"""
# def find(source,target,start=0,end=''):
#     if target in source:
#         if isinstance(end,str):
#             end = len(source)
#         for i in range(start,end):
#             if source[i:len(target)+i] == target:
#                 return i
#     else:
#         return -1
# print(find('ddddddabddddaddd','ab',3,5))

"""
3.计算字符串中所有数字的和，已知字符串中都是字母和数字

- 比如传递 '12abc34def5lala'  返回 12+34+5=51
- 比如传递 'lov12e4dudu5baby'  返回 12+4+5=21
"""
# def computer(s2):
#     import re
#     res = [ float(x)  for x in re.findall(r'\d+\.?\d*',s2)]
#     return sum(res)
# print(computer("sd234kjxjv3.21"))

"""
4.传入数字n，求出 1^1 + 2^2 + 3^3 + ... n^n 的和
"""
# def sum1(n):
#     return sum([ x**x for x in range(1,n+1)])
#
# print(sum1(5))

""""
5.明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1～1000之间的随机整数(N<=1000),
N是用户输入的，对于其中重复的数字，只保留一个，把其余相同的数字去掉，不同的数对应着不同的学生的学号，然后再把这些数从小到大排序，按照排好的顺序去找同学做调查，请你协助明明完成“去重”与排序工作。

"""
def demo(n):
    import random
    l1 = list(set([random.randint(1,1000) for x in range(n)]))
    l1.sort()
    return l1

"""
"""

