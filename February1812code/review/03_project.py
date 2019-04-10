# if里面的代码块,要么就执行,要么就不执行
# if True:
#     print('ok')

# 这个选择结构.一定会选择一个分支进行代码执行
# if True:
#     print('ok')
# else:
#     print('no')

# if -elif -else:从多分支中,选择一个分支,进行代码的执行
# day = input('请输入一个数:')
# if day.isdigit():
#     day = int(day)
#     if 0 < day < 8:
#         if day == 1:
#             print('星期一')
#         elif day == 2:
#             print('星期二')
#         elif day == 3:
#             print('星期三')
#         elif day == 4:
#             print('星期四')
#         elif day == 5:
#             print('星期五')
#         elif day == 6:
#             print('星期六')
#         else:
#             print('星期天')
#     else:
#         print('输入的数字不正确!')
# else:
#     print('输入不正确!')


# 从键盘输入一个数,求出最大数,最小数
# num1 = int(input('第一个数:'))
# num2 = int(input('第二位数:'))
# num3 = int(input('第三位数:'))
# min = num1
# max = num1
# if min > num2:
#     min = num2
# if min > num3:
#     min = num3
# if max < num2:
#     max = num2
# if max < num3:
#     max = num3
# print('最大数为{},最小数为{}'.format(max,min))

# 加号由两种用法:
# 1.数学加
# print(1+2)
# 2.拼接:字符串拼接
# print('hello'+'world')

# 在java中,可以用字符串加别的类型,将别的类型也转成字符串输出
# Python2支持,Python3不支持
# print('hello'+123)  #TypeError: must be str, not int
# try:
#     print('hello'+123)
#
# except Exception as e:
#     print(e)

# 数学运算符: + - * / // **                 结果:数字
# 赋值运算符: =  +=  -= *= /=  //= **=      结果:将值由右边赋值到左边
# 比较运算符:  <  >  <= >=  != ==           结果:布尔值

#因为实际工作中,需要满足多个条件才能进行下一步操作,这里就是可以逻辑运算符

# and  并且   逻辑与
#小明要考驾照,必须满足:  1.年龄是18到70之间
                       # 2.money>=5000
                       # 3.不能是色盲
# age = 20
# money = 6000
# isColorBlind = False
# if  18<=age<=70  and  money>=5000 and isColorBlind == False:
#     print("可以考驾照")

#18 <= age <= 70     这种链式比较,python支持.python会自动优化为   age>=18  and  age<=70
#  真  and  真  ==>真
#  真  and  假  ==>假
#  假  and  真  ==>假
#  假  and  假  ==>假
#总结: 两个为真,才为真

#如果有多个and,那么按照顺序由左到右进行运算.
#(x>100 and  y<10) and  z == 1000


# or   或者   逻辑或
# 小明需要去做飞机旅游.  有其中一个证件,就可以坐飞机
# 1.  可以使用身份证登机
# 2.  使用军官证
# 3.  使用港澳通行证,护照
# isHaveID = False
# isHaveOfficer = False
# isHaveHK_ID = True
# if isHaveID or isHaveOfficer or isHaveHK_ID:
#     print("可以乘坐飞机")

# 真  or  真 ==>真
# 真  or  假 ==>真
# 假  or  真 ==>真
# 假  or  假 ==>假
# 结论:  有一个真,结果就为真


# not  取反   逻辑非
# 判断一个数是不是奇数
# num = int(input("请输入一个数:"))
# if num%2 :
#     print("是奇数")
# else:
#     print("是偶数")


# not  True  => False
# not  False => True
# not 这个运算符,返回一个布尔值
# num = int(input("请输入一个数:"))
# if  not num%2 :   #如果num%2==1,那么这个1代码True. 对这个1进行取反,就会得到False,那么就会得到偶数
#     print("是偶数")
# else:
#     print("是奇数")
#
# 当num =4时,   num%2==0,  not 0 ==>True    => 打印出偶数
# print( not  4 )  #False
# print( not  0 )  #True

# num = 'asasa' or None or 'sb' or 'hello'
# print(num)
#
# # 函数
# # print()
# def a():            #def() 定义函数,a是函数名.():括号中放参数
#     print('A')
#     return True     #调用这个函数,返回True
# # num = a()     #调用函数   函数定义时,函数体并不会被执行
#         # 只有调用函数时,它的函数体才会被执行
# # print(num)      #如果函数有return,那么调用这个函数,可以获取的return的结果
#
# def b():
#     print('B')
#     print()
#     return False
#
# def c():
#     print('c')
#     return True
#
# # 短路特性
# # and短路   如果and的第一个条件为假,那么后面的条件无论真假,该表达式的结果都为假
# if a() and b() and c():
#     print('ok')
#
# if a() or b() or c():
#     print('ok')

# # in  判断这个值是否出现在列表,字典中
# list1 = [1,2,3,4,5]
# print( 1 in list1 )   #判断1这个数字是否在list1中
# print( 9 in list1 )
#
# # not in  不在列表中返回真,在列表中返回假.
# print( 2 not in list1 )   #False
# print( 9 not in list1)    #True

# is : 判断两个变量内部的地址是否相同
# == : 判断两个变量指向的值是否相同

# a = 10
# b = a
# print(  id(a) )
# print(  id(b) )
# print( a is b )    #这两个变量所存储的地址相同

# #因为有常量池的存在,所以使用这个常量的变量,都是是同一个地址
# x = 20
# y = 20
# print(  id(x)  )
# print(  id(y)  )
# print(  x  is  y)
#
# y = 100           #给y变量赋值另外一个常量,那么y变量保存的地址就会被修改
# print( id(x))
# print( id(y))
# print(  x is y)     #False
# print( x  is not y) #判断x和y变量的内存地址为不同.  True

# # 总结: is比较的是变量存储的内存地址
#
# string1 = 10
# string2 = 10
#
# string1 = "hello world"
# string2 = "hello world"
# print(string1 is string2)
# print( string1 == string2 )   #比较变量指向的值是否相等.  hello == hello
#
#
# list2 = [1,2,3,4]    #list2指向一个对象
# list3 = [1,2,3,4]    #list3指向另一个对象
# print(  id(list2) )
# print(  id(list3) )
# print( list2 is list3 )  #False
# print( list2 == list3 )  #True     内容一致

# if 5-5:
#     print("ok")
#
# if 5>5:
#     print("ok")

# if a += 4:      #if后面不能接赋值语句
#     print("ok")
#     print("ok")

#需求:  打印10000次hello world

i=1      #循环变量
while i<= 5:      #i  = 1  2  3  4  5
    # print("hello world")
    i += 1        #循环变量的自增

# 这个循环结构代码执行步骤
# 1.设置循环变量初值
# 2.执行while判断.
#    成立:   -->执行循环体  ->再来执行while判断 ->成立或不成立
#    不成立: 循环结束


#因为循环条件永远成立,所以这是死循环
j = 1
while True:
    if j>=5:
        break           #强制结束循环,break之后的代码不会被执行
        print("6666666")  #这句话不会被执行到
    # print("ok")
    j += 1


# 总结:如何写循环结构
# 1.创建一个循环变量
# 2.通过while进行判断
# 3.循环变量一定要发生变化

# while 表达式:
#
# else:

#当表达式成立时,就执行循环体. 当表达式不成立时,就执行else.  else只会被执行一次
# num = 1
# sum = 0
# while num <= 100:
#     sum += num
#     num +=1
# else:
#     print(sum)
#     print("从1加到100完成")



#使用break强制结束循环,不会触发else
# 使用break可以有效的减少无用循环
count = 1
while count<=10:
    if count == 2:
        break
    # print("hello world")
    count += 1
else:
    print("打印10次hello world完成")

#统计100~1000之间能被6整数的数的个数
# count = 0  #计数器
# num = 100  #循环变量
# while num <= 1000:
#     if num%6 == 0:
#         count += 1
#     num += 1
#
# print(count)

#3.计算10的阶乘
#  10*9*8*7*6*5*4*3*2*1
num = 10
total = 1
while num>=1:
    total *= num
    num -= 1

print( "10的阶乘是:",total )

#循环嵌套一般是两层
# 1*1=1
# 1*2=2  2*2=4
# 1*3=3  2*3=6  3*3=9

# 九九乘法表逻辑:
# 1.需要打印9行
# 2.每一行中,打印对应的乘法结果

#第1行,只打印1次
#第2行,打印2次
row = 1
while row <= 9:
    i = 1
    while i<= row:
        # print( i,"*",row,"=",i*row,end=" " )  #打印后,不换行
        i += 1
    # print("")    #打印空字符,实际上取的是换行
    row += 1

# row = 1   ,  i=  1
# row = 2   ,  i = 1  2
# row = 3   ,  i = 1  2  3
#内层循环用于控制打印次数.  外层循环用于控制行数
rrow = 9
for i in range(1,rrow+1):
    for item in range(1,i+1):
        pass
        # print('{}*{}={}'.format(item,i,i*item),end='\t')
    # print('')
