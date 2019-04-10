# 1.自定义一个数字列表，获取这个列表中的最小值，并将列表转化为元组
# list1 = [1,5,9,12,8,6,100]
# min = list1[0]         #找最小数,不能直接给零.因为可列表中的数,都比0大,就会产生错误
#                       #假设第0个数为最小数
# for item in list1:
#     if item<min:
#         min = item
#
# print(min)
# print( tuple(list1) )


# 2.自定义一个数字列表，元素为10个,找出列表中最大数连同下标一起输出
# list1 = [1,5,9,12,8,6,100,88,99,77]
# max = list1[0]
# max_index = 0
# for index,item in enumerate(list1):
#     #找到最大数,那么当前下标也是最大
#     if max<item:
#         max = item
#         max_index = index
# print(max,max_index)


# 3.自定义一个数字列表，求列表中第二大数的下标
# list1 = [1,5,9,12,8,6,100,88,99,77]
# list2 = list1.copy()
#
# #找最大数
# max = list2[0]
# for item in list2:
#     if item > max:
#         max = item
# 移除
# list2.remove(max)

#找次大数
# second = list2[0]
# for item in list2:
#     if item > second:
#         second = item

#获取次大数,在list1中的下标
# print(    list1.index(second)  )


# 4.B哥去参加青年歌手大奖赛,有10个评委打分,(去掉一个最高分一个最低分)求平均分
# score = [8.7,9.5,7.0,9.0,9.5,8.9,8.8,9.0,7.8,9.4]
# max =  score[0]
# min = score[0]
# for item in score:
#     if item<min:
#         min = item
#     if item>max:
#         max = item
# score.remove(max)
# score.remove(min)
# sum =0
# for item in score:
#     sum += item
# print(  sum/len(score) )

# 5.定义元组，存放5个学生的成绩【成绩值自己设定】，获得成绩之和，平均成绩，最小成绩，最大成绩。



# 6.已知列表list = [34,55,67,88,99,100],使用二分法查找67在列表中的位置



# 1.将一个列表逆序输出
# list1 = ["a","d","c","b"]

#切片
# print( list1[::-1] )

#插入
# list2 = []  #定义一个空列表
# for item in list1:
#     list2.insert(0,item)   #一直往空列表的第0个元素插入
# print(list2)

#交换
#交换次数需要除以2
# for i in range(len(list1)//2):
#     list1[i],list1[-i-1] = list1[-i-1],list1[i]
# print(list1)



# 2.输入某年某月某日，判断这一天是这一年的第几天
# list1 = [31,28,31,30,31,30,31,31,30,31,30,31]    #每月天数列表
# year = int(input("请输入年:"))
# month = int(input("请输入月:"))
# day = int(input("请输入日:"))

#判断是平年还是闰年
#如果是闰年,2月天数加1
# if (year%4==0 and year%100!=0) or year%400==0:
#     list1[1] += 1
#
# sum = 0
# for i in range(month-1):    #month=1   2   3
                            #当month为1是,这个for循环不会被执行,那么就会直接打印day
    #将每个月的天数加起来
    # sum += list1[i]

#月份的天数+day天数
# print(sum + day)


# 3.给定一个列表：将列表中指定的某个元素全部删除
# list1 = [1,2,2,2,2,2,2,2,4,4]
# i = 0
# while  i< len(list1):
#     if list1[i] == 2:
#         del  list1[i]
#         #i-=1           #移除元素后,下标往前挪一次
#         continue        #可以使用continue,让后面的下标增加操作取消
#     i += 1
# print(list1)

# 4.自定义一个列表，最大的与第一个元素交换，最小的与最后一个元素交换，输出列表
# list1 = [3,6,4,9,20,7,5]
# max = max(list1)
# max_index = list1.index(max)
# list1[0],list1[max_index] = list1[max_index],list1[0]
#
# min = min(list1)
# min_index = list1.index(min)
# list1[-1],list1[min_index] = list1[min_index],list1[-1]
#
# print(list1)


# 5.在控制台输入一句英语，获得每个字母出现的次数，注：每个字符作为key，出现的次数作为value生成一个字典
# string = "hello world"
# dict1 = {}
# for char in string:   #char是string的每个字符串
#     dict1[char] = string.count(char)     #dict1["h"] = string.count("h")
#
# print( dict1 )

#练习: 不基于count函数,去求出出现次数最多的元素,和次数
#基于比较来获取最多次数
#实现的逻辑:
# 1.拿列表中第0个元素,去和后面的每个元素进行比较,如果相等则计数器加1
# 2.使用一个max变量,接受最大次数
# 3.使用max_item变量,接受多次数元素
# list1 = [1,5,5,5,5,5,5,4,4,3,3,3]
# max = 0
# max_item = None
# for i in  range(len(list1)):
#     #第一次比完1之后,第二次比5,那么需要将计数器归零
#     count = 0
#     for j in range(i,len(list1)):  #当i = 0  j = 0  1 2 3 4 5...      list[i]:1   list[j]:  1  5 5 5 5 5 4 4 4
#                                    #当i = 1   j = 1  2 3 4 5 6 ...    list[i]:5    list[j]: 5 5 5 5 5 4 4 4
#         if list1[i] == list1[j]:
#             count += 1
#
#             if count>max:
#                 max = count
#                 max_item = list1[i]
# print( "最多次数:",max,"最多次数字符:",max_item )


#总结: 第一层for循环,用于遍历列表中的每个数
    # 第二层for循环,在前面i的基础上,先和自己进行比较,然后在和列表中后面所有的数进行比较


#练习: 不基于set进行列表去重    [1,2,2,2,4,4,4,4]        删除元素时,注意这个跳过的问题
#去重的逻辑: 拿一个数,去和列表中后面的所有数进行比较,如果发现有相同的,那么把后面这个数删除
# list1 = [1,2,2,2,4,4,4,4]
# i = 0
# while i< len(list1):
#     j = i+1
#     while j<len(list1): #因为这个数不需要和自己进行比较,所以这里进行+1
#         if list1[i] == list1[j]:
#             del  list1[j]
#             continue       #删除后,下标不要加1,继续进行下一次比较
#         j+=1
#     i+=1
#
# print( list1 )

#set其实就是一个只有key的字典. 所以set中就是无序的
#set去重可能乱序
# list1 = [1,2,2,2,4,4,4,4,2,4,1]
# set1 = set(list1)
# list2 = list(set1)
# print(list2)

#求出现最多次数的元素
list3 = [1,2,2,2,2,5,5,7,7,7,7,7,7,7]
dict1 = {}
for item in list3:  #遍历每一个元素
    if item not in dict1: #如果这个元素不在字典中
        dict1[item] = list3.count(item)    #将元素做键,将次数做值,存入字典中
# print(dict1)

#获取最多次数元素
max = 0
max_item = None
for key,value in dict1.items():
    #如果次数,大于最多次
    if value>max:
        #那么就修改
        max = value
        #已将找到了最多次数,那么当前的key,就是最多次数的元素
        max_item = key
# print("做多次数元素:",max_item,"最多次数:",max)


# 集合(set):  只有key,没有value的一个字典
# 根据这个原理可以得到:
# 1.字典中的key不允许重复,所以set中也不会出现重复的元素
# 2.字典中的key只能是不可变对象,所以set中也只能放置不可变对象

#第一种创建集合的方式
# set1 = {1,2,3,4,5,5,5,5,5}
# print( set1 )
# print( type(set1))

#第二种创建集合,借用list,元组,字符串,字典
# list1 = ["a","b","c","d"]
# set3 = set(list1)
# print(set3)

# tuple1 = ("a","b","c","d")
# set4 = set(tuple1)
# print(set4)

#自动去重
# string = "hello"
# set5 = set(string)
# print(set5)

#只会获取键,组成集合
# dict1 = {"name":"xiaoming","age":20,"money":1000}
# set6 = set(dict1)
# print(set6)

#这样不会认为是一个空集合,会认为是一个空字典
# dict1 ={}
# print( type(dict1))

#创建空集合只能使用set()
# set7 = set()
# print(set7)
# print( type(set7))

#添加元素
# set7.add(1)
# set7.add(1)       #如果元素已经存在,那么会被自动去重,添加就无效了


#因为集合中都是key,key不允许使用可变对象.
#可变对象:    list   dict
#不可变对象:  tuple   number  string

#程序崩溃后,后面的代表不会被执行.
# set7.add([4,5,6])  #列表不允许被加入     TypeError: unhashable type: 'list'
# set7.add({"name":"xiaoming"})  #字典不允许被加入     TypeError: unhashable type: 'dict'

# set7.add(2)    #允许加数字
# set7.add("hello")  #字符串允许
# set7.add( ("a","b","c") ) #元组允许
# print(set7)

# update()   将括号内的参数,进行遍历,然后将每个元素加入到集合中.所以这个参数不能是数字,因为数字无法被遍历
# set8 = set()
# set8.update([1,2,3])
# set8.update([1,2,7])
# set8.update((4,5,6))
# # print("set8:",set8)
#
# set8.update("hello")
#
# # print("set8:",set8)
#
# set8.update({"name":"xiaoming","age":20})
# # set8.update(100)    #数字不允许
# # print("set8:",set8)
#
# #删除指定元素
# # set8.remove("name")
# set8.remove('name')
#
# #删除不存在的元素,会崩溃
# # set8.remove(10)
# # set8.remove(10)
# set8.discard(10)
# #使用discard删除元素时,不存在也不会崩溃
# # set8.discard("name")
# set8.discard('name')
# print(set8)
#
# # 遍历集合
# #遍历集合中的每个元素
# for item in set8:
#     print(item)
#
# #这个index只是位置编号,不能作为索引来使用
# for index,item in enumerate(set8):
#     print(index,item)
#
# #集合不支持下标
# # print( set8[0])
#
# set9 =  {1,2,3,4}
# set10 = {3,4,5,6}
# #求交集.         返回由两个集合都存在元素所组成的集合
# set11 = set9 & set10
# print(set11)
#
# #求并集          返回两个集合的所有元素组成的集合,去重
# set12 = set9 | set10
# print(set12)

#冒泡求最大数.    将大的数放到最后面
# list1 = [4,9,20,16,7,8,40,23]   #先进行4和9的比较,不交换.  进行9和20的比较,不交换. 进行20和16的比较,交换
# list1 = [4,9,16,20,7,8,40,23]   #进行20和7的比较,交换
# list1 = [4,9,16,7,20,8,40,23]   #进行20和8的比较,交换
# list1 = [4,9,16,7,8,20,40,23]   #进行20和40的比较,不交换    进行40和23的比较,交换
# list1 = [4,9,16,7,8,20,23,40]   #进行一轮比较后的结果

list1 = [4,9,16,7,8,20,23,40]

# #因为这个out会取到列表的最大值,再加1就越界了.所以在外层循环这里减1
# for out in range(len(list1)-1):
#     for inner in range(len(list1)-out-1):  #因为每一轮排序都会确定一个最大的放到最后面,所以下次循环就可以少一次比较
#         if list1[inner] < list1[inner+1]:           #inner = 0    inner+1 = 1    list[0] > list[1]
#             list1[inner],list1[inner+1] = list1[inner+1],list1[inner]  #交换
#
# print( list1 )

#冒泡排序时,只需修改比较的大于符号或小于符号,就可以得到升序或则降序列表

# for out in range(len(list1)-1):
#     for inner in range(len(list1)-1-out):
#         if list1[inner]>=list1[inner+1]:
#             list1[inner],list1[inner+1]=list1[inner+1],list1[inner]
# print(list1)

#先寻找最小数的下标,先记录下来.  最后只进行一次交换即可.
# list1 = [4,9,16,7,8,20,3,23,40]
#先认为第0个元素就是最小  ==>4

#遍历这个列表,去寻找比这个4更小的数. 找到就把这个下标存储起来
# list1 = [4,9,16,7,8,20,(3),23,40]

#通过上面的比较,就已经得知了最小数的下标,那么就拿这个数和第0个数进行交换
# list1 = [3,9,16,7,8,20,4,23,40]

# list1 = [3,(9),16,7,8,20,4,23,40]
# list1 = [3,9,16,7,8,20,(4),23,40]
# list1 = [3,4,16,7,8,20,9,23,40]
#选择排序会进行多次比较,但是只会进行一次交换

list1 = [4,9,16,7,8,20,3,1,23,40,99,88]
# for out in range(len(list1)):
#     #使用min变量,保存最小数下标
#     #out循环变量会变大,代表前面的下标已经排好序了,不在需要参与比较了
#     min_index = out
#     for inner in range(out+1,len(list1)):
#         if list1[inner] < list1[min_index]:
#             #找到了比list[min_index]更小数的下标,进行替换
#             min_index = inner
#
#     #进行一次交换即可
#     list1[out],list1[min_index] = list1[min_index],list1[out]
#
# print(list1)
#
# #out = 0    min_index=0   inner = 1 ,2,3,4,5,6,7,8
#                    #  list[1]<list[0]  list[2]<list[0]   list[3]<list[0]...
#
#
# #同理,只需修改选择排序的比较符号,同样可以修改为升序,或降序

# for out in range(len(list1)):
#     min_index = out
#     for inner in range(out,len(list1)):
#         if list1[min_index]>list1[inner]:
#             min_index = inner
#     list1[min_index],list1[out] = list1[out],list1[min_index]
# print(list1)

# 1.顺序查找: 遍历列表,挨个进行比较
# list1 = [1,5,9,14,27,88,100]
# key = 27
# for index,item in enumerate(list1):
#     if item == key:
#         print("找到了,下标是:",index)
#         break

# 2.二分查找(折半查找). 基于一个有序列表
# list1 = [1,5,9,14,27,88,100]
# left = 0              #left最开始指向第0个元素
# right = len(list1)-1  #right最开始指向最后一个元素
# key = 99              #要查找的数
# while left <= right:
#     middle = (left+right)//2
#
#     # 我们要找的数,比中间这个数大.意味着它在右侧
#     if  key > list1[middle]:
#             left = middle + 1
#
#     #要找到的数,比中间这个数小,意味着它在左侧
#     elif key < list1[middle]:
#             right = middle-1
#     else:
#         print("找到了,下标是:", middle)
#         break
# else:
#     print("这个数不存在该列表中")


#  left      middle          right
# [   1,5,9,    14,   27,88, 100]
#
#               left middle  right
# [ 1,5,9,14,   27,    88,   100]
#
#                            left
#                            right
#                            middle
# [ 1,5,9,14,   27,    88,   100]



# key = 99
#  left      middle          right
# [   1,5,9,    14,   27,88, 100]

#               left middle  right
# [ 1,5,9,14,   27,    88,   100]


#                            left
#                            right
#                            middle
# [ 1,5,9,14,   27,    88,   100]


#这个时候出现left > right,循环条件不成立,结束查找
#                            left
#                      right
# [ 1,5,9,14,   27,    88,   100]

# 字符串: 由多个字符所组成的列表.  但是字符串是不可变的,所以不能修改它.

#c语言字符串
#char[] = "hello"

# 字符串类型:str

#空串.  字符串支持单引号或双引号.  注意:空格也算字符
string1 = ""
string2 = ''

#多行字符串.   换行符虽然不可见,但是也是字符串的一部分.  这个string3算真
string3 = """
"""

string4 = '''
'''

#空串代表false
if string3:
    print("True")
else:
    print("False")

#字符串中可以包含任意字符
string5 = "hello你好good조선글"
print(string5)

#字符串的相加
#因为字符串不可变,所以对字符进行任何操作,均不会改变自身.只会返回一个操作的结果
string6 = "hello"
string7 = "world"
string8 = string6 + string7
print(string8)
print(string6)
print(string7)


#python中支持相同的数据类型进行运算
# print( "hello"+3 )
# print( "1">3 )

#重复
print( string6*3 )

#因为字符串本质上也是列表,所以也可以通过索引进行元素的获取
# print( string6[0] )
# print( string6[-1] )
# print( string6[100])     #越界

#字符串不能修改
# string6[0] = "x"


#字符串的遍历和列表的遍历,没有区别
# string : 字符串
# char   : 字符
string = "helloworld"

#获取每个字符
for char in string:
    print(char)

#通过下标遍历
for index in range(len(string)):
    print(string[index])

#通过下标,字符的形式遍历
for index,char in enumerate(string):
    print(index,char)


#字符串的切片和列表的切片,没有任何区别
string2 = "abcdefg"
print( string2[1:4] )
print( string2[:4] )
print( string2[4:] )
print( string2[-4:] )
print( string2[::-1] )


#in  判断子字符串是否在父串中.   检索整个字符串,去判断在不在
print( "a" in string2 )
print( "abc" in string2 )
print( "deg" in string2 )
print( "a" not in string2 )

#空格的ascii码是32
print(  ord(" ")  )


name = "xiaoming"
age = 20

#逗号会变成一个空格
print("name=",name,"age=",age)

#使用格式化输出,就可以保证输出的效果和字符串一模一样
print( "name=%s,age=%d"%(name,age) )

# %s   字符串
# %d   整数
# %f   小数

#保留4位小数
# print( "%.4f"%(3.1415926)  )

#需要8位字符,如果不够,前面补空格
# print( "%8s"%("hello") )


#需要打印""
print( "\"hello\"" )

# \n  换行
# \t  tab
# \b  backspace  按一下退格键
print( "hello\nworld" )
print( "hello\tworld" )
print( "hello\bworld" )
print( '\'' )
print( "\"" )
print( "\\" )


#使用字符串表示文件路径
# path = "D:\工作\Python\03_Linux"   #03不能打印
#path = "D:\工作\Python\nomal"        #\n会当做换行处理

#在字符串前面加上r,代表忽略转义
path = r"D:\工作\Python\nomal"

#也可以在普通字符串前面加r
print( r"good" )
print(path)

