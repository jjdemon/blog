# 模块:它就是一个py文件,里面可以有很多的函数和变量

import random   #导入产生随机数的模块

# 列表(数组)
# stu_list = ['asa','asas','dsddsdsd','asasasas']

# for i in range(3):
#     string = random.choice(stu_list)
#     print(string)
#
#     stu_list.remove(string)

# list1 = ['qwwew','wewewew','sasasas']
# for i in range(1):
#     string = random.choice(list1)
#     print(string)
#     list1.remove(string)

# -32  =>  原码:10100000  反码:11011111  补码:11100000
#             反码:10011111    补码:10100000 => -32

# if
# not
# and
# or
# False
# True
# 如果这个单词颜色不是黑色,那么它就是关键字

# 保留字:在Python以后的版本中,可能会变成关键字    goto

# 保留字和关键字,不允许作为变量名

# 使用变量是为了解决数学问题.
# 使用算法,解决逻辑问题
# 有一辆车速度为59km/h,B车是它速度的2倍还要多2km/h,求B车的速度.
# x = 59*2+5      # x在数学中称之为未知数,在编程中称之为变量
# x = 100*2+5     # 数学中未知数的值允许发生变化,编程中变量的值也允许发生变化

# 变量:一个值允许发生变化的量
# 关键字不允许当做变量名
# if=5    错误示例    #SyntaxError: invalid syntax

# 变量的名字,叫做标识符
a = 10  # a就是标识符

# 标识符的命名规则:
# 1.尽量要做到见名识意     sum = 0  count = 0
# 2.只能由字母/数字/下划线所组成,其不能以数字开头
# 3.为了方便阅读,使用驼峰原则(单词首字母大写)
# 4.严格区分大小写

# 1a = 10           非法标识符
# a1 = 10           合法字符
# abc@qwe = 10      非法字符
# _abc = 10         合法字符
# student_list_Python1812 = ['张三','lisi'] #使用下划线分隔单词,变量的首字母小写
# studentListPython1812 = ['zhangsan','lisi']     #使用单词首字母大写分离
# age = 10
# print(Age)  #严格区分大小写    报错: name 'Age' is not defined

# 标识符的作用:命名变量,命名函数,命名类

# Python是一门弱类型的编程语言,他的变量类型需要通过值来倒退.

# Python中,变量一定要赋初值
# Python中有7种基本数据类型:
# 1.数字Number
a = 10+2    #赋值,将整数10赋值给变量a.    赋值符运算从右到左
print(type(a))  #type() 求出括号中参数的类型  int

b = 5.12
print(type(b))  # float 浮点数小数

c = 2+3j        #复数,2是实部部分,3j是虚数部分
print(type(c))  # complex 复数

d = True
print(type(d))  # bool 布尔值

# 2.字符串 str.  单引号括起来,或双引号括起来的字符
# 双引号不能嵌套双引号,单引号也不能嵌套单引号
string1 = "hello world  @#$%^&&  "
string2 = 'zhagnsan'
string3 = "hell'123'o"
stirng4 = '小明说:"你好"'
stirng5 = "小明说:\"你好\""    # \"    转义字符,让这个引号正常输出
stirng6 = "\\"                 #因为\用来做转义,所以打印\,要两个
print( type(stirng6))         #str

# 3.列表  list
myList = ["a","b","c"]
print( type(myList) )

# 4.元组  tuple.  不让改
myTuple = (1,2,3,4,5)
print( type(myTuple))

# 5.字典  dict.   里面存储的是键值对      键:值
myDic = {"name":"xiaoming","age":"20"}
print( myDic["name"] )    #通过name这个键,获取值
print( type(myDic)  )

# 6.集合  set.   去重
mySet =  set(myList) #通过列表创建集合
mySet2 = {3,4,5,6,7,8,8,8,8,8,8}      #通过大括号来创建集合



mySet3 = {}                           #这种产生并不是空集合,而是空字典
print( type(mySet))
print( mySet2)
print( type(mySet3))

# 7.空    None.    一般为对象设置初值为None
print( None )
print( type(None) )    #NoneType

#如何对列表去重:  转成集合即可
list1 = [1,1,2,2,3,3,4,4]
set1 = set(list1)      #set()   将参数转集合
list2 = list(set1)     #list()  将参数转列表
print(list2)


#变量的内容可以随意设置
a = 10
a = "hello"
a = [66,77,88]
print(a)

b = "10"      #字符串b
b = int(b)    #将字符串b转成整数,还赋值给变量b
print(b,type(b))   #print函数中的逗号,代表空格

# 常量: 不允许修改的量
print(100)
print( 3+4j )
print("hello")
print( True )

#python约定用全部大写的字母,表示常量.
NUM = 100

# + - * /    数学运算
x = 3
y = 4
print( x*y )    #12

# 赋初值
# 数字初值
a = 0
# 字符串初值
string = ""
#布尔初值
isFinish =  False
#列表初值
myList = []

# 变量一定要先声明才能使用
# print(num)

result = x * y   #声明一个变量result,它的内容是x*y的乘积
print(result)

# a = 100
# b = 200
# print(a)   #取出a指向堆内存那片区域中,所保存的值
# print(b)
#
# # id()   返回参数的内存地址
# print( id(a) )   #栈内存中,变量a所存储的地址
# print( id(b) )   #栈内存中,变量b所存储的地址

# a = 100
# b = a
# 这段代码,在C语言中. 将100放入a变量中.然后将a内的100取出来,在放入b中
# 在python中,  a=100,就在栈内存中,开一个房间,放入变量a,a的内容是100在堆内存中的地址.
#  再让b=a,实际上是在栈内存开一个房间,放入变量b,b的内容和a变量的内容是一样的.
#  python的变量间赋值,拷贝的不是100这个数,而是变量内部存储的地址

# print(  id(a)  )    #地址相同
# print(  id(b)  )    #地址相同

a = 100
b = a
b = "hello"

print( id(a) )
print( id(b) )

# python为什么将数字,字符串放入堆内存,因为python一切皆对象.普通的数字也是对象.


#删除变量 del
num = 100
print(num)

del num
# print(num)           变量被删除,房间就会被回收.这个变量无法再被使用

a = 100
b = 100

#这两个地址一致
print(  id(a) )
print(  id(b)  )

#python需要使用到常量时,首先会在常量池创建这个常量.当有变量使用到这个常量时,就会将这个变量指过来.
# 当第二次使用这个常量时,因为这个常量已经存在,所以它不会创建第二次,会直接引用第一次的这个常量.

# x = 3
# y = 4
# print( "x*y =",x*y )   #打印时带上前缀

#从键盘接受值,input会让程序暂停
#python只支持  字符串加字符串或则数字加数字.   不支持字符串加数字
# num = input("请输入一个数:")
# print( type(num) )       #str
# num = float(num)           #将字符串转数字
# print( num + 100)

#转整数,丢弃小数位
# print(  int(4.66)  )


# 示例:输入长,宽,求面积
# 如果代码出现函数的嵌套调用.最先调用的内层函数,然后再调用外层函数
# width = int(    input("请输入宽度:")   )
# length =int(    input("请输入长度:")   )
# print("面积是:",width*length)

# str()   将参数转字符串
# int()   将参数转整数
# float() 将参数转浮点数

# print(   str(100)   )
# print( type(str(100)))
#
# print( int(3.1415) )
# print( int("100") )
# print( int("a") )    #转换非数字,会崩溃

#实际工作中,需要先对字符串先校验,再进行转换.避免转换失败造成程序崩溃
# if "aaa".isdigit():     #判断是不是数字类型字符串
#     print("Yes")
# else:
#     print("No")

print( float("3.1415926"))
print( float(10) )       #10.0

# + - *  /  加减乘除
# %    求余(取模)
# //   整除(只取整数的商),又称地板除

# print( 3%2 )  #1
# print( 6%8 )  #6
# print( 14%7 ) #0

# 一个数对2取余,得1则为奇数.得0则为偶数
# print( 5%2)  #1
# print( 8%2)  #0


# print( 10/4 )  #2.5    结果有小数,就会显示小数
# print( 10//4 ) #2      整除,只取整数位的商

# **  求多少次方(幂)
# print(2**2)   #4         2的2次方
# print(2**10)  #1024      2的10次方
# print(3**4)  #81

# 求一个三位数的个位,十位,百位
# num = 345
# ge = num%10
# shi = num%100//10
# bai = num//100
# print("百:",bai,"十:",shi,"个:",ge)


# print( 2**10*4 )  #先算2的10次方,再乘以4


# +=  -= *= /= //= **=    复合赋值运算符
num = 10
num += 2   #   等同于num = num+2
num **= 2  #  num = num ** 2
print(num)

#比较运算符   <  >  <=  >=  == !=
#比较运算返回布尔值 True 或则False
# == 代表比较值,它不是赋值
# print( 3>5 )
# print( 3<5 )
# print( 3==3 )
# print( 3!=3 )

# 位运算: 先将操作数转成二进制,在来进行运算.
# 实际上计算机进行加减乘除都是进行位运算.
# &  按位与      两个1结果为1,否则为0
print( 4&5 )  #0100  &  0101   => 0100

# 0100
# 0101   &
# ----
# 0100

# |  按位或    只要有1个1,结果就为1.
print(4|5)     #5
# 0100
# 0101   |
# ----
# 0101

# ^  按位异或     相同为0,不同为1
print(4^5)      #1
# 0100
# 0101   ^
# ----
# 0001

# ~  按位取反
print( ~5 )    #   00000101  =>   (补码)11111010->  反 11111001 ->原 10000110     -6

# << 左移      将这个二进制数整体向左移动,空出来的位补0. 移动时,符号位不变
#左移只会,数会变大    m*2**n   ==>6*2**2
print(6<<2)  #  00000110    =>  00011000   =>  24

# >> 右移动   右移之后,如果符号位为0,则补0.    如果符号位为1,则补1
print(6>>2)  # 00000110   =>   00000001  =>  1
print(-6>>2) # 10000110原   =>   11111001反 =>  11111010补  => 11111110 结果 =>反11111101   =>原10000010

# 编程时,存在三种结构
# 1.顺序结构:  代码从第一行执行到最后一行
# 2.选择结构:  代码执行到if时,选择走if,还是else
# 3.循环结构:  代码执行到while,for时,会多次执行循环体

#顺序结构
# a = 10
# a = 20
# print(a)

#选择结构
# x = int(  input("请输入一个数:")  )
# if x>10:        #如果这个条件成立,那么执行OK, 如果这条件不成立,则执行NO
#     print("OK")
# else:
#     print("NO")

#如果只有if可以是做选择的.  成立就执行代码,不成立就略过
# if x<100:
#     print("这个数小于100")


#可以用这些值来表示False,   0 ""  None  False  0.0
#表示为True的值            非0,非空字符串,Ture,非零浮点数
#实际工作中,基本上不会使用True和False来做选择.一般都是通过运算结果来判断

if  5-5:
    print("成立")
else:
    print("不成立")


