# list1 = [True,False,True,False,1,2,2,1]
#
# count = list1.count(1)
# print(count)
#
# print( True == 1)   #在python中布尔值True,它的数字形式就是1
# print( False == 0)  #在python中布尔值False,它的数字形式就是0
#
# # 在python2中,没有True和False,它就是用1和0来表示.

# 从键盘输入一个数n,判断是不是一个质数(质数只能被1和它自身整除的数)
# def fn(num):
#     for i in range(2,num):
#         if num % i == 0 :   #能够除尽,从2到自己-1,代表它是一个合数
#             return False
#     return True
#
# num = int(input('请输入一个数:'))
# # isPrime = True
# if num<2:
#     print('输入数字不正确')
# else:
#     # for i in range(2,num):
#     #     if num % i == 0 :   #能够除尽,从2到自己-1,代表它是一个合数
#     #         isPrime = False
#     #         break
#     #
#     # if isPrime == True:
#     #     print('这个数是质数')
#     # else:
#     #     print('这个数是合数')
#     print(fn(num))
#
# 5.计算1到500以内能被7整除但不是偶数的数的个数。
# count = 0
# for i in range(1,500):
#     if  i%7==0   and  i%2 != 0:
#         count += 1
# print(count)


#封装一个函数,传入一个数,如果是质数返回True,如果是合数,返回False
# def  fn(num):
#     for i in range(2,num):
#         if num%i == 0:
#             return False    #在函数中使用return,会直接结束函数.包括正在执行的循环
#                             #函数中只会执行一次return
#     return True

# 1.
# 从键盘输入一个数n，判断是不是一个质数（质数是只能被1和它自身整除的数）
# num  = int(input("请输入一个数:"))
# isPrime = True    #这是一个布尔值标识位,默认认为这个数是质数
#
# if num <2 :
#     print("输入的数字不正确")
# else:
    # for i in range(2,num):   #2~num-1
    #     if num%i ==0:    #这个数能够除尽,从2到自己-1,代表它是一个合数
    #         isPrime = False
    #         break

    # 待上面for循环执行完毕,再来判断
    # if isPrime:
    #     print("是质数")
    # else:
    #     print("是合数")


    # 调用函数.            函数需要现在上面声明,下面才能调用
    # print(   fn(num)   )



# 2.
# 求1000以内的水仙花数：
# 水仙花数：一个三位数各个位上的立方之和，等于本身。
# 例如： 153 = 1（3） + 5（3）+ 3（3） = 1 + 125 + 27 = 153
# for i in range(100,1000):
#     bai = i//100
#     shi = i%100//10
#     ge = i%10
#     if bai**3 + shi**3 + ge**3 == i:
#         print(i)


# 3.
# 求2～100
# 之内的素数。【素数 ： 只能被1或本身整除的数】



# 4.
# 优化猜数字游戏
#
# 计算机出一个1
# ~100
# 之间的随机数由人来猜
# 计算机根据人猜的数字分别给出提示大一点 / 小一点 / 猜对了，这个过程可以循环进行，当进行5次以上还猜不对的话，则打印：智商余额不足
# import  random
# num = random.choice(range(1,100))   #1~99
# num = random.randint(1,100)         #1~100
# print(num)
# for i in range(5):
#     myInput = int(input("请输入一个数:"))
#     if myInput == num:
#         print("猜对了")
#         break                 #执行break,for后面的else不会被执行
#     elif myInput< num:
#         print("大一点")
#     else:
#         print("小一点")
# else:
#     print("智商余额不足")

# list1 = [-6,9,20,-12,33]
# 这个key是一个函数.
# list1.sort(key=abs)  #让list1中的每个元素,都去调用abs函数.在通过调用函数返回的结果进行排序
#
# list2 = ["hello","z","good"]
# list2.sort(key=len)
#
# print(list1)
# print(list2)



#for in 遍历
# list1 = ["a","d","b","d","c","d","d","d","d"]
# for item in  list1:
#     print( item )   #这个item就是列表中的每个元素.并且不能被修改
#     item = "66666"   #修改无效
#
# print(list1)

#for in 遍历,这个循环变量不能被修改
#如果想实现循环变量的修改,请使用while
# for i in range(10):
#     print(i)
#     i = 4            #修改无效

#失败,存在删除丢失的问题
# for item in list1:
#     if item == "d":
#         list1.remove(item)
# print(list1)

#解决办法1:  先求出这个元素出现的次数,再删除那么多次
# count = list1.count("d")
# for i in range(count):
#     list1.remove("d")   #执行count次删除操作
#

# print(list1)

#解决办法2:  删除元素后,遍历指针不往后移,让它减1
# for i in range(len(list1)):
#     # if list1[i] == "d":
#     #     list1.remove("d")   #因为我们在执行删除d这个操作,删除了元素,列表会变小
#
#     print(i)
#     i -= 1             #修改无效


# 如果想修改循环变量,那么需要使用while
# i = 0
# while i< len(list1):
#     if list1[i] == "d":
#         list1.remove("d")
#         i -= 1         #删除之后,遍历指针不往后移,原地停留
#     i+=1
#
# print(list1)

# 总结: for i in range(len(list1)): 遍历开始时,就确定了i的只是0~列表长度减1. 遍历过程中不会发生变化.
# while i < len(list1)    如果遍历时,删除list1中的元素,那么len(list1)就是实时变小


#a.表达式从左向右进行计算，如果or的左边的逻辑值为True，则整个表达式的值为True，则短路or后面的所有的表达式【不管是and还是or】

#b.表达式从左至右运算，若 and 的左侧逻辑值为 False ，则短路其后所有 and 表达式，直到有 or 出现，输出 and 左侧表达式到 or 的左侧
# ，参与接下来的逻辑运算。

def true():
    print("1212")
    return  'ffgdfg'
def false():
    print("33")
    return False

#print( True or False and True)   #or的左侧出现了True,会短路
#true() or false() and true()      #or后面被短路

#false() and false() and false()    #如果表达中只有and,那么and第一个位false,那么会短路后面所有的and
#false() and true()  and false() or true()  #如果and的第一个为false,那么会短路后面所有的and,直至or出现
# print(true() and false()  and true() and true() or false())


# list1 = [1,4,4,4,4,2,2,2]
# max = 0
# max_item = None
# for item in list1:
#     count = list1.count(item)     #求出每个元素的次数
#     # print(count)
#     if count> max:                 #如果次数大于max
#         max = count              #那么就替换max
#         max_item = item          #既然现在找到了最多次数,那么现在这个item就是出现最多次数的item

# print( "次数:",max,"元素:",max_item )



#练习: 不基于count函数,去求出出现次数最多的元素,和次数
#练习: 不基于set进行列表去重    [1,2,2,2,4,4,4,4]        删除元素时,注意这个跳过的问题

#求出现最多次数的元素
# list3 = [1,2,2,2,2,5,5,7,7,7,7,7,7,7,7]
# dict1 = {}
#
# # break  直接结束整个循环,如果循环后面有else,这个else也不会被执行
#
# # for i in range(10):
# #     print(i)
# #     if i == 5:
# #         break
# # else:
# #     print("遍历结束")
#
#
# #break直接结束当前所在的循环
# # for i in range(10):
# #     for j in range(20,31):
# #         print(j)
# #         if j == 25:
# #             break          #break只结束当前所在的循环
# #     print(i)
#
#
# # continue  结束本次循环,直接进行下一次循环
#
# # for i in range(10):
# #     if i==5:
# #         continue    #结束本次循环.  循环体后面的代码不执行
# #     print( i )
#
#
# #求列表中所有数字的和
# list1 = [1,6,"hello","good",20,None]
# sum = 0
# for item in list1:
#     if type(item) != int:   #如果这个元素的类型不是数字,那么全部略过
#         continue
#     sum += item
#
# # print(sum)
#
# # pass  为了让代码能够运行通过,使用的一个占位符
# if True:
#     pass
#
# # while True:       #先使用占位符,让程序能够通过,以后再来实现
# #     pass
#
#
# # 最多使用是在程序的设计阶段. 先把程序的所有功能先定义好,不着急实现.以后再来实现
# def addStudent(stu):
#     pass
#
# def removeStudent(stu):
#     pass
#
# # 从右到左,挨个赋值
# num1 = num2 = num3 = 20
# print(num1)
#
# #将30赋值给num4,  将40赋值给num5
# (num4,num5) = (30,40)
# tuple1 = num6,num7 = 100,200     #元组可省略括号
# print(tuple1)
# print(type(   tuple1   ))
# print( num4)
# y,*_,x = [1,2,3,4,5]
# print(x,*_[::-1],y)
#
# #变量的值交换
# # 1.使用第三个变量交换
# x = 3
# y = 4
# # z = y   #1.使用第三个变量来接受
# # y = x   #2.首尾相连即可
# # x = z
# # print(x,y)
#
# # 2不使用第三个变量进行交换
# # 2.1 使用元组,python特有
# # y,x = x,y
# # print(x,y)
#
# # 2.2 使用加法
# # x = x + y   #7 = 3+4
# # y = x - y   #3 = 7-4
# # x = x - y   #4 = 7-3
# # print(x,y)
#
# # 2.3 使用异或
# # x = x^y        #0111=0011^0100
# # y = x^y        #0011=0111^0100
# # x = x^y        #0100=0111^0011
# # print(x,y)
#
# print( int("2") )
# print( float("2.45"))
# # print( int("abc123")  )    #非数字,转换失败   isdigit()
#
# print( int("+30"))   #正数
# # print( int("3+0"))   #非法
#
# print(int("-30"))  #负数
# # print(int("3-1"))  #非法
#
# print( int(3.45))  #3
# #print( int("3.45"))  #仅能转换整形的字符串数字,带小数不行
# print( int(float("3.45")) )  #需要先转浮点数,再取整

# print(abs(-7))  #求绝对值
# print(abs(-7))
#max函数支持两种参数. 一种是放一个可迭代对象(列表),一种是放多个参数.
# print( max(3,7,9))
# print(max(3,7,9))

# list1 = [5,20,6]
# # print( max(list1))
#
# #同理,也可以获得最小数
# print( min(3,7,9))
# print( min(list1))
#
# #x**y  求指数
# print( pow(2,10))   #求2的10次方
# print(pow(2,11))
#
# #round 四舍五入
# print( round(3.6) )
# print( round(3.4) )
# print( round(3.5) )

#round(数字,保留位数)   保留位数的时候,进行四舍五入
# print( round(3.66123,3))
# print( round(3.66183,3))

#小数在计算机中存储是无理数,这个5就相当于是4123121232的约等于,所以这个3.675它只能得到3.67
# print( round(3.675,2 ) )    #可以理解为5舍6入
# print(round(2.2324,2))

#建议工作中,尽量不要使用round,而是用ceil 和 floor

# import  math
# print( math.ceil(3.7))  #天花板    向上取整: 求大于该数的最小整数
# print( math.ceil(3.1))
# print(math.ceil(3.4))
# print(math.ceil(3.6))
#
# print( math.floor(3.7)) #地板    向下取整: 求小于该数的最大整数
# print( math.floor(3.1))
# print(math.floor(3.6))
# print(math.floor(3.2))
#
# print( math.sqrt(16) )  #开平方
# print(math.sqrt(25))
# print(math.sqrt(9))
#
# print( math.modf(34.15))  #将这个数转成元组的形式,第一个是小数,第二个是整数
# print(math.modf(22.14))
# print(math.modf(223.22))

# import random
# randint 从(x,y)这个范围内,随机取一个整数,并且 x<=n<=y
# print(random.randint(1,10))     #包含1,包含10
# print(random.randint(1,10))
#
# #random.choice 从一个序列中,随机取一个数
# print(random.choice(range(1,10)))      #包含1不包含10
# print(random.choice(range(1,3)))
#
# list1 = ['a','b','c','d']
# print(random.choice(list1))     #随机从列表中取一个
# print(random.choice('hello'))   #随机从hello中返回一个字符
#
# print(random.choice(range(10)))
# print(random.randrange(10))
# print(random.randrange(5,20,4))

# 返回一个0-1的随机数,浮点数     0<n<1
# print(random.random())

# 将列表中的元素,随机排序
# list2 = ['a','b','c','d','e']
# random.shuffle(list2)   #没有返回值,直接修改这个列表
# print(list2)
# 返回一个3-10之间的随机数,浮点数
# print(random.uniform(3,10))     #3<n<10

# 元组: 只读的列表
# tuple1 = ()   #空元组
# tuple2 = (1,2,3,4,5)
# tuple3 = (2,"hello",True)
# #
# print( type(tuple1))
# print( tuple2)
# print( type(tuple2))
# print( type(tuple3) )

# tuple4 = (5+4)  #括号用于提升优先级
# tuple5 = (5)    #这个括号不会当做元组,会当成数字处理
# print( tuple4 )
# print( type(tuple5) )
#
# tuple6 = (5,)     #如果元组只有一个元素,需要多加一个逗号,否则会被当做数字处理
# print( tuple6)
# print( type(tuple6))


# 元组中的元素,只允许被读取,不允许被修改
# tuple7 = ("a","b","c","d")
#
# 元组也是有序列表,可以通过索引获取
# print( tuple7[0] )
# print( tuple7[-2] )

# print( tuple7[10] )   #元组越界

# tuple7[2] = "hello"     #元组中的元素,不允许被修改

# tuple8 = (1,2,3,4,[5,6,7])
# tuple8[-1] = "hello"     #不允许修改.  这里修改的是整个元素

# tuple8[-1][0] = 20    #整个列表作为整体不允许被修改,但是列表中的元素,允许被修改
# print( tuple8)


#元组可以被整体删除
# del tuple8           #删除就相当于整个变量未声明
# print(tuple8)


# + 合并元组
tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# tuple3 = tuple1+tuple2   #合并元组后,返回新元组
#
# print(tuple3)
#
# print( tuple1*3 )    #重复3次
# print(tuple1)

# print( 1 in tuple1 )  #在这个元组中就返回True
# print( 1 not in tuple1 )  #不在返回True

#和列表一样,支持切片
# print( tuple1[1:] )
# print( tuple1[-1:] )
# print( tuple1[:2] )

# print( tuple1[::-1])

# print( len(tuple1) ) #求长度
# print( max(tuple1) )
# print( min(tuple1) )

# 元组和列表互转
# list1 = ["a","b","c"]
# print(   tuple(list1)    )   #列表转元组

# print( list(  ("a","b","c")   ) )   #元组转列表

#遍历的三种方式
# tuple2 = (4,5,6)
# # 1.for in
# for item in tuple2:
#     print(item)
#
# # 2. 使用下标遍历
# for i in range(len(tuple2)):
#     print(tuple2[i])
#
# # 3,使用枚举遍历
# for index,item in enumerate(tuple2):
#     print(index,item)

#二维元组
# tuple3 = ( ("a","b","c"),(1,2,3),("A","B","C") )
# for item in tuple3:   #("a","b","c")
#     for item2 in  item:
#         print(item2)

# dict1 = {}  #空字典

# dict2 = {"name":"xiaoming","age":20}  #字典中存储的是键值对. key:value的形式
# print(dict2)
# print( type(dict2))

#字典中的key只允许出现一次.后面会覆盖前面
# dict3 = {"name":"xiaoming","age":20,"name":"zhangsan"}
# print(dict3)

#不可变:  数字,字符串,元组
#可变:    列表
#key只能使用不可变类型
# dict4 = {"name":"xiaoming",10:100,(1,2,3):"good"}
# print(dict4)

#列表不能作为字典的键
# dict5 = {[1,2,3]:"hello"}
# print(dict5)


#字典的访问:     通过键来获取值
dict5 = {"name":"xiaoming","age":20,"money":20}    #键不能重复,但是值可以
# print(   dict5["hello"]  )   #如果该键不存在,则崩溃

#get函数.  如果该key存在,则返回value. 若该key不存在,则返回None. 不会崩溃
# result = dict5.get("name")
# print(result)
# result = dict4.get(10)
# print(result)
# result = dict4.get((1,2,3))
# print(result)
# result = dict5.get('age')
# print(result)
#
# if result:    #如果result为None,则代表false
#     print("存在这个键")
# else:
#     print("不存在这个键")


#字典的添加和修改语法是一样的
# dict6 = {"name":"xiaoming"}

#添加一个键值对
# dict6["sex"] = "男"          #dict[key] = value
# print(dict6)

#修改一个键值对
# dict6["name"] = "zhangsan"
# print(dict6)

# dict[key] = value   对于不存在的键,则是添加.对于存在的键,就是修改


# dict7 = {"name":"xiaoming","age":20,"sex":"男"}
#删除
# 1.pop  弹出: 删除这个键值对,返回值
# result = dict7.pop("name")
# print(result)

# 2. del 纯删
# del dict7["name"]
#
# print(dict7)

dict1 = {"name":"xiaoming","age":20,"sex":"男"}

#如果对字典使用for in 语法,那么这个循环变量就是key
# for key in dict1:
#     print(key,"=",dict1[key])
# for key in dict1:
#     print(key,'=',dict1[key])

#获取所有键
# key_list = dict1.keys()   #以列表的形式,返回有的键
# for key in key_list:
#     print(key)

# for key in dict1.keys():
#     print(key,'=',dict1[key])

#获取所有的值
# value_list = dict1.values()  #以列表的形式,返回有的值
# for value in value_list:
#     print(value)
# for value in dict1.values():
#     print(value)


#获取所有的键值
result = dict1.items()   #以列表的形式返回所有的键值对,每个键值对都是元组的形式
# print(result)            #dict_items([('name', 'xiaoming'), ('age', 20), ('sex', '男')])
# for (key,value) in result:   #直接通过元组的形式,遍历这个列表
#     print(key,"=",value)

#等同上面这个循环
# for key,value in dict1.items():
#     print(key,value)
# for key,value in dict1.items():
#     print(key,'=',value)

#以枚举的形式遍历. 这个index只是key在字典中的序号,实际用来获取元素
for index,key in enumerate(dict1):
    print(index,key,dict1[key])
    # print(dict1[key])     #value

# print( dict1[0] )   #错误

#1.逐一显示指定字典中的所有键，并在显示结束之后输出总键数
dict1 = {"name":"xiaoming","age":20,"sex":"男"}

#方法1
count = 0
for key in dict1:
    print(key)
    count +=1    #每执行一次循环,代表有一个键,那么就加1
else:
    print(count)  #打印

#方法2
for key in dict1:
    print(key)
else:
    print(  len(dict1  ))   #直接打印字典内键值对的个数

#2.list1 = [0,1,2,3,4,5,6],list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"].以list1中的元素作为key，
# 以list2中的元组作为value生成一个新的字典dict2
list1 = [0,1,2,3,4,5,6]
list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
dict2 = {}
#因为键值必须成对出现,所以这两个列表必须等长
if len(list1) == len(list2):
    for i in range(len(list1)):  #以下标的方式遍历列表
        # key                value
        # list1[i]           list2[i]
        dict2[ list1[i]  ] =  list2[i]

print(dict2)


#求出现最多次数的元素
list3 = [1,2,2,2,2,5,5,7,7,7,7,7,7,7,7]
dict1 = {}