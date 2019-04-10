import itertools
import time


# count创建一个无限迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cycle将传入的序列无限重复下去
# cs = itertools.cycle('abc')
# for c in cs:
#     print(c)

# repeat将一个元素重复下去，第二个参数可指定重复次数
# ns = itertools.repeat('ABC', 3)
# for n in ns:
#     print(n)

# takewhile可根据条件判断截取一个有限序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x:x<=10,natuals)
# print(list(ns))

# chain可以把一组迭代对象串联起来，形成一个更大的迭代器
# for i in itertools.chain('ABC', '123', 'hhh'):
#     print(i)

# groupby把迭代器中相邻的重复元素挑出来放一起
# for key, group in itertools.groupby('aaffFFfkkkmmddnnndl'):
#     print(key, list(group))

# 忽略大小写
# for key, group in itertools.groupby('aaffFFfkkkmmddnnndl', lambda f: f.upper()):
#     print(key, list(group))

# 计算圆周率
# 计算公式：4/1 - 4/3 + 4/5 - 4/7 + 4/9 ...
def pi(n):
    print('计算中...')
    s = time.time()
    cs = itertools.cycle([4, -4])
    odd = itertools.count(1, 2)
    sum = 0
    for i in range(1, n):
        sum += next(cs) / next(odd)
    e = time.time()
    print('结果为：%s,计算耗时：%.3f秒' % (sum, e - s))


pi(100000000)







