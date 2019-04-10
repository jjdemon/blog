# 列表(数组):一个容器,用于放置多个相同的数据类型的变量
# 作用:将多个元素按照顺序存储在一起,方便进行计算

# 链表存储数据内存空间可以不连接, 数组(列表)存储数据内存空间必须连续
# list1 = [1,2,3,4]
# list2 = ['a','b','c','d']
# list3 = [1,'hello',True,None]   #列表其实也能放不同的数据类型
#
# list4 = []      #空列表

# print(list3)
# 元素(成员): 列表中每个变量就是元素
list2 = ["a","b","c","d"]
# 使用索引(下标)获取其中一个元素.  索引值的取值范围 0~长度-1
# print( list2[0] )    #获取第0个元素
# print( list2[-1])    #获取倒数第1个元素

#如果使用的索引,超出了列表的长度-1,那么就会产生越界问题
# print(list2[5])      IndexError: list index out of range
# print(list2[-10])    IndexError: list index out of range


#有多个变量,需要求和
# age1 = 10
# age2 = 20
# age3 = 30
#
# list3 = [age1,age2,age3]
# print(   sum(list3)   )    #sum函数可以放入一个列表,用于对列表所有元素求和

#替换元素
list2[2] = "hello"    #列表的元素,可以被替换
# print(list2)


# 删除元素
del list2[2:4]   #删除列表中索引为2的元素

# 增删改会修改列表,查不修改列表
# print(list2)

# 1.合并列表,使用+
list1 = [1,2,3,4]
list2 = ["a","b","c","d"]
list3 = list1 + list2     #按照顺序将列表合并
# print( list3 )

#2.重复列表  使用*
list4 = ["a","b","c"]
list5 = list4 * 3
# print(list5)

#去重
set1 = set(list5)
list6 = list(set1)
# print(set1)
# print(list6)      #set只能保证无重复,但是不能保证是原来的顺序


#判断元素是否在列表中
# print( "a" in list2)        #判断字符串a是否在list2中,在返回True
# print( "a" not in list2)    #判断字符串a是否在list2中,不在返回True

# 切片: 提取列表部分元素所组成的子列表
# 公式:  [起始:结束:步进]       从起始截取到结束,以步进为单位.
#        [start:end:step]       包头不包尾.    [1:3],截取的是1到3但是不包含3

# list1 = ["a","b","c","d","e","f"]
# print( list1[3]   )   #获取一个元素,返回的这个元素,它的类型是字符串
# print( list1[-2]  )
#
# print( list1[1:4] )  #"[ b","c","d"]
# print( list1[4:1] )  #[]   如果end小于start,那么返回一个空列表
#
# print( list1[0:4])  #["a","b","c","d"]
# print( list1[:4])   #如果省略start那么代表从第0位开始截取
#
# print( list1[4:6])    #['e', 'f']
# print( list1[4:100])  #end可以超出上限,代表从start开始,截取后面整个列表.  这个100等同于6
# print( list1[4:])     #如果省略end,代表取到最末尾

# 切片还可以使用负数
# print( list1[-4:-1] )  #从倒数第4个取到倒数第1个,不包含倒数第一个
# print( list1[-1:-4])   #[]     切片默认只能从左到右,不能从右到左
# print( list1[:-3] )   #从0取到倒数第3个,不包含倒数第三个
# print( list1[-4:])    #从倒数第四个取到最末尾

# print(list1[100:200])

#使用step
# print( list1[0:5:2])  #从第0个取到第4个,每次取后面第二个
# print( list1[3::2])  #从第3个取到最末尾,每次取后面第二个

#复制列表
# list2 = list1[::]
# print(list2)
# print( id(list1))   #两个列表的内存地址不一样
# print( id(list2))   #两个列表的内存地址不一样

# step使用负数.  代表从后往前取
# list3 = list1[::-1]    #倒着取每个,实际上就是将列表反转
# list3 = list1[::-2]    #倒着隔两个
# print(list3)

# print( list1[4:1:-1] ) #默认start要小于end,但是使用负数步进时,start可以大于end

# print( list1[-2:-4:-1] )
# print(list1)          #切片不会对原列表产生任何影响

# 功能,函数,方法,function

#list1[2]         读取,不修改原列表
#list1[2] = 100   设置,会修改原列表
#del list1[2]    删除,会修改原列表
#list1[1:5]     切片,也是读取,不会修改原列表

list1 = ["a","b","c","d","e","f","e","e"]
# 1.增加   append
#功能:  在列表尾部,追加一个元素
#返回值:    None
#是否修改原列表:   是
# result = list1.append("g")
# result = list1.append("h","i")        append仅能追加一个元素
# result = list1.append('as')
# print(result)
# print( list1 )

#追加一个子列表
# list1.append(["h","i"])            #追加后会变成二维列表
# print(list1)

# 2.extend()     扩展列表
#功能:  在列表尾部,进行扩展.   使用扩展的参数是一个列表,执行扩展后,会将两个列表合并
#返回值:           None
#是否修改原列表:   是
# result = list1.extend(["g","h"])
# result = list1.extend(['g','i'])
# print(result)
# print(list1)   #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# 3. insert(index,object)    插入元素
#功能:      在列表的索引位置,插入元素
#返回值:           None
# 是否修改原列表:   是
# result = list1.insert(0,"hello")
# print(result)
# print(list1)


#4. pop     从列表弹出一个元素
#功能:      从列表弹出一个元素,并且间将这个元素从列表中移除.默认弹出最后一个
#返回值:           被弹出的元素
#是否修改原列表:   是
# result = list1.pop()   #如果不给参,实际上弹出的最后一个
# print(result)
# print(list1)

# result = list1.pop(3)    #弹出指定索引的元素
# print(result)
# print(list1)


# 5. remove     从列表移除一个元素.  从左到右移除找到的第一个
# 功能:         从列表移除一个元素.  从左到右移除找到的第一个
#返回值:           None
#是否修改原列表:   是
# result = list1.remove("e")    #移除指定的元素.  只会移除一次,若想全部移除,请使用循环
# count1 = list1.count('e')
# for item in range(list1.count('e')):
#     result = list1.remove('e')
# print(result)
# print(list1)


#6. del    通过索引移除
# del list1[3]
# del list1[2]
# del list1[1]
# print(list1)

#总结: 使用索引移除, del  pop.   使用元素对比移除, remove

#7.清空列表
#功能:         清空列表
#返回值:           None
#是否修改原列表:   是
# result = list1.clear()
# result = list1.clear()
# print(result)
# print(list1)

# len()  返回列表的长度

# list1 = [1,2,3,4,5]
# print( len(list1) )       #length
# print( len("helloworld") )
# print( max(list1) )     #返回列表中的最大值
# print( min(list1) )     #返回列表中的最小值

# list2 = ["a","b","c","b","f","b","g","b"]
# print(    list2.index("b")  )    #返回b这个元素在list2中的索引,默认返回找到的第一个
# print(list2.index('b'))
# print(list2.index('b',6,100))
# print(    list2.index("b",4,100) )  #在list2第4个索引到第100个索引之间,寻找第一个b元素
#
# print( list2.count("b") )     #统计b元素在list2中出现的次数
# for i,item in enumerate(list2):
#     print(i,item)

# reverse   将列表倒序.无返回值,会修改原列表
# result = list2.reverse()
# result = list2.reverse()
# print(result)


# print(list2)


#sort  将列表进行排序.默认为升序. 如果是字符串,那么比较的ascII码
#  无返回值,直接修改原列表
# result = list2.sort()
# result = list2.sort()
# print(result)
# print(list2)

#  字符串比较规则: 依次比较字符串的每一位,直至必出大小为止
# list3 = ["hello","lily","lilei","jhon"]
# result=list3.sort(reverse=True)
# result = list3.sort(reverse = True)
# print(result)
# print(list3)
#
# list4 = [34,21,9,5,30]
# list4.sort(reverse=True)    #降序排列
# print(list4)

#使用绝对值来排序
# list5 = [34,-21,9,-5,30]
# list5.sort( key=abs  )         #key后面接一个用于排序的函数.  按照绝对值来排序
# print(list5)

# print(   abs(-6)  )          #求绝对值

#比较字符串的长度
# list7 = ["congratulations","aa","hello","nice"]
# list7.sort(  key=len,reverse=True )  #让每个元素都来调用len函数获取长度,再通过这个长度排序
# list7.sort(key= len,reverse = True)
# print(list7)


# sorted  对列表进行排序.返回一个排序好的新列表.对原列表不影响
# sort 直接对列表进行排序.   serted返回排序好的新列表,不影响原列表,生成一个副本
# result = sorted(list7,key=len,reverse=True)
# result = sorted(list7,key=len,reverse=True)
# print(result)
# print(list7)

# python  变量的复制分为3种
# 1.对象间引用.
#
# 不可变对象. 数字,字符串,元组,None
# num1 = 10
# num2 = num1
# print(id(num1))
# print(id(num2))
#
# num2 = 100
# print(num1)
# print(id(num1))
# print(id(num2))
# 总结:  对于不可变对象,使用赋值符号做对象间引用.修改其中一个不会影响另一个
#
# 可变对象.   列表,字典,集合
# list1 = ["a","b","c"]
# list2 = list1     #实质上是两个变量指向堆内存中的同一片空间.一改齐改
# print(id(list1))
# print(id(list2))
#
# list2[1] =  "hello"
# print(id(list1))
# print(id(list2))
# print(list1)
# print(list2)

# 2.浅复制
# list1 = ["a","b",[1,2]]
# list2 = list1.copy()
# list2 = list1.copy()     #浅复制

# print(id(list1))
# print(id(list2))
# list2[0] = "hello"     #对于外层列表,它们是独立的
# print(list1)
# print(list2)

# print(id(list1))
# print(id(list2))

# list2[-1].append(3)   #对于内层列表,它们指的是同一片内存空间
# print(list1)
# print(list2)


# 3深复制
# import  copy
# list1 = ["a","b","c",[1,2]]
# list2 = copy.deepcopy(list1)    #让两个变量完全独立
# list2 = copy.deepcopy(list1)
# list2 = copy.deepcopy(list1)
# list2 = copy.deepcopy(list1)
# print(id(list1))
# print(id(list2))
# list2[-1].append(3)
# list2[1] = 'c'
# print(list2)
# print(list1)
# print(id(list1))
# print(id(list2))

#需求:移除列表中所有的23
# list30 = [23,435,5656,6767,435,23,23,54,64,5676,23,23,23]

# list30.remove(23)  #只能移除一次
# print(list30)

# list30.remove(10)  #remove必须移除列表中存在的数,如果不存在就会崩溃

# 先求出有多少个23,再来做移除
# count = list30.count(23)

#循环次数是count次
# for i in range(count):
#     list30.remove(23)
# print(list30)


#使用判断来移除(有bug)
# for item in list30:         #遍历list30列表,item是每个元素
#     if item == 23:
#         list30.remove(item)
# print(list30)

#因为删除前面这个23后,遍历的指针会自动后移,但是删除一个元素后,列表元素自动前移动,导致有两个23无法被删除
# 所以使用for in 遍历列表时,最好不要做删除操作
# [23,54,64,5676,23,23,23]

#
# list1 = [
#     [1,2,3,4],
#     ["a","b","c","d"],
# ]
#
# print(  list1[0]  )   #第0个元素,是一个子列表
# print(  list1[0][2] )  #取第0个元素中,第2个元素
#
# class1 = ["xiaoming","lily"]
# class2 = ["lilei","zhangsan"]
# grade = [class1,class2]
# print(grade)


#for   循环用于遍历列表
# 遍历: 挨个访问列表中的元素
#
# list1 = ["a","b","c","d"]
# for item in  list1:
#     print(item)      #每个元素
# else:
#     print("遍历完毕")
#
# #通过下标遍历
# for i in range(   len(list1)   ):  # 0~4     ==>0 1 2 3
#     print(list1[i])
# else:
#     print("遍历完毕")
#
#
# #使用枚举函数,遍历下标和元素
# # for (i,item) in enumerate(list1):
#     # print("下标是:",i,"元素是:",item)
#
# for i,item in enumerate(list1):
#     print(i,item)

# range(start,stop,step)  生成从start到stop的一个列表,不包含stop. 可以使用setp
#range  列表生成器

#求50到100的和
# sum = 0
# for i in range(50,101):
#     sum += i
# print(sum)
#
# #求50到100所有的偶数和
# sum= 0
# for i in range(50,101,2):
#     sum += i
# print(sum)
#
# for x in range(10,20):
#     print( x )  # 10 11 12 13 14 15 16 17 18 19



# 九九乘法表
# for i in range(1,10):  #1~9
#     for j in range(1,i+1):    #i=1   j= 1
#                               #i=2   j= 1 2
#         print(j,"*",i,"=",j*i,end=" ")
#
#     print("")

#1.显示列表list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]中索引为奇数的元素
# list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# for i in range(len(list1)):   #使用下标遍历整个列表
#     if i%2:                  #奇数个下标
#         print(list1[i])


#2.将属于list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，但不属于
# list2 = ["Sun","Wed","Thu","Sat"]的所有的元素组成一个新的列表list3
# list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# list2 = ["Sun","Wed","Thu","Sat"]
# list3 = []
# for item in list1:         #获取list1中的每个元素
#     if item not in list2:  #这个元素在list1中,不在list2中
#         list3.append(item)
# print(list3)


#3.已知列表list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，removeList = ["Sun","Wed","Thu","Sat"],
#将属于removeList的元素从list1中全部删除【注意：属于removeList，但不属于list1的直接忽略】\
# list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# removeList = ["Sun","Wed","Thu","Sat",1]
#
# #删除list1中,出现在removeList中出现了元素
# for item in removeList:
#     if item in list1:
#         list1.remove(item)
#
# print(list1)

