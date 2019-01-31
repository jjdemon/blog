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

import random
# randint 从(x,y)这个范围内,随机取一个整数,并且 x<=n<=y
print(random.randint(1,10))     #包含1,包含10
print(random.randint(1,10))

#random.choice 从一个序列中,随机取一个数
print(random.choice(range(1,10)))      #包含1不包含10
print(random.choice(range(1,3)))

list1 = ['a','b','c','d']
print(random.choice(list1))     #随机从列表中取一个
print(random.choice('hello'))   #随机从hello中返回一个字符

print(random.choice(range(10)))
print(random.randrange(10))
