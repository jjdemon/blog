# 初级：
#1.声明变量时不要使用str,list,tuple,dict,set,int,float这些关键字做变量名.
# list = [1,2,3]
# print( list("hello") )

# 2.自己创建的py文件,文件名不要和关键字同名(导入的模块同名),可能会发生异常
# import random
# print(    random.random()  )

# 1.已知字符串：“this is a test of Python”
str1 = "this is a test of Python"
# print( str1.count("s") )
# 	a.统计该字符串中字母s出现的次数

# 	b.取出子字符串“test”
# index = str1.find("test")              #找到test的下标
# print( str1[index:index+len("test")])   # 使用切片  str1[下标:下标+4]

# 	c.采用不同的方式将字符串倒序输出
# print( str1[::-1] )

#先转列表,在调用reverse,在转回字符串
# list1 = list(str1)
# print(list1)
# list1.reverse()
# print(list1)
# print( "".join(list1) )

#遍历字符串,从后往前遍历
new_str = ""
for i in range(len(str1)-1,-1,-1):    #range(10,-1,-1)    步长为负,可以start大于end.   10,9,8,7,6,5,4,3,2,1,0
    new_str += str1[i]
print(new_str)

# 	d.将其中的"test"替换为"exam"
# print(  str1.replace("test","exam"))

# 2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
# 	a.请将a字符串的大写改为小写，小写改为大写
a = "aAsmr3idd4bgs7Dlsf9eAF"
# print( a.swapcase())

# 	b.请将a字符串的数字取出，并输出成一个新的字符串
# new_str = ""
# for char in a:
#     if char.isdigit(): #是数字
#         new_str += char
# print(new_str)

# 	c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
# dict1 = {}
# a = a.lower()  #全部转小写,再统计.达到不区分大小写
# for char in a:
#     if char.isalpha():
#         #将写入字典的次数,减少到1次
#         if char not in dict1:
#             dict1[char] = a.count(char)   #字母做键,次数做值
# print(dict1)

# 	d.输出a字符串出现频率最高的字母
# max = 0
# max_char = ""
# for char in a:
#     #只统计字母,数字不统计
#     if char.isalpha():
#         count = a.count(char)   #统计每个字母出现的次数
#         if count>max:
#             max = count
#             max_char = char  #当前次数就是最多次,那么这个字符就是最多次字符
# print( "次数:%d,字符:%s"%(max,max_char) )

# 	e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False
# str2 = "ADF"
# for char in str2:   #遍历str2中的每个字符
#     if char not in a:  #如果出现这个字符不在a中
#         print(False)   #打印False
#         break          #直接结束循环,包括else
# else:
#     print(True)       #遍历结束,都没有打印出False,代表都在.  所以可以输出True


# 1.去除字符串两端的指定字符
# str1 = "****hello****world*******"
# key = "*"
#系统函数
# print( str1.strip("*") )

# 从0开始判断,这个字符是不是*,是*,就count+1,然后切片
#先除去前面的*
# count = 0
# for i in  range(len(str1)):
#     # 是*,就计数器增加
#     if str1[i] == key:
#         count +=1
#     else:
#         # 不是,就立刻结束循环
#         break
# str1 = str1[count:]   #切片,从count,切到最末尾
# print(str1)

#除去后面的*
# count = 0
# for i in  range(len(str1)-1,-1,-1):   #range(10,-1,-1):   从10遍历到0
#     if str1[i] == key:
#         count += 1
#     else:
#         break
# str1 = str1[:len(str1)-count]
# print( str1 )


#实现字符串插入功能
str1 = "helloworld"
insert_str = "123"
insert_index = 3

#1.转列表,再插
# list1 = list(str1)
# list1.insert(insert_index,insert_str)  #插入
# result = "".join(list1)
# print(result)

#切片,切成两段,在拼接
sub1 = str1[:insert_index]   # 0~3      hel
sub2 = str1[insert_index:]   # 3~末尾   loworld
result = sub1 + insert_str + sub2
print(result)


# times new roman 字体
#需求澄清

# def change(list1):
#     list1[1],list1[3] = list1[3],list1[1]
#     print("函数内:",list1)
# list0=[1,2,3,4]
# print( "原列表:",list0)
# change(list0)
# print( "函数外:",list0)

