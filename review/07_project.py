# list1 = [5,9,2,4,13,6]
#
# #控制比较的轮数
# for out in range(len(list1)-1):    #为什么减1,因为进行多次比较后,列表已经有序了.最后一次就不需要进行
#
# #两两比较,如果前面的数,大于后面的数,就交换位置
# #这个for循环,就是一轮排序
#     for i in range(len(list1)-out-1):  #为什么-out-1:  -1:因为i+1会越界,所以要减1
#                                        # -out-1:   进行一轮交换后,最大数已经确定在最末尾,那么最末尾这个数就可以不参与比较了
#         if list1[i]>list1[i+1]:
#             list1[i],list1[i+1] = list1[i+1],list1[i]
#
# print(list1)


# len()  可以作用于字符串,列表,元组,字典,集合,用于获取长度

# print( len(123))    数字没有长度
# print( len("hello") )

# str1 = "hello world hello world"

#统计子串在父串中出现的次数
# print(  str1.count("hello") )   #统计整个字符串

# print( str1.count("o",12,1000) )  #分区间计数.  统计o在12到最末尾出现的次数


#对字符进行任何操作,都是拿返回值,自己不会变

# 大小写转换

# 将字符串中所有大写字母转小写,非字母不处理
# str2 = "Today Is a good day  123123 ^*&"
# # str3 = str2.lower()
# # print(str3)    #返回一个处理后的结果
# # print( str2 )  #原串不变
#
# #转大写:  将所有字母转大写,非字母原样输出
# #使用:  如果项目中需要进行不区分小写比较,那么可以将整个字符串转大写再比,或者将整个字符串转小写再比
# str4 = str2.upper()
# str4 = str2.upper()
# print( str4)
#
# #将字符串的大小写反转
# str5 = str2.swapcase()
# str5 = str2.swapcase()
# print( str5)
#
# #将整个字符串的首字母大写
# str6 = "hello world"
# str7 = str6.capitalize()
# str7 = str6.capitalize()
# print(str7)
#
# #将每个单词的首字母大写
# str8 = str2.title()
# str8 = str2.title()
# print(str8)

# str()   将参数转为字符串类型

# result1 = str(123)         #支持数字
# print(result1)
# print( type(result1))
#
# #因为变量在内存中,就是一个地址. 那么在前后交互时,是无法传递整个地址的.所以都是将变量转字符串,再传递
# result2 = str([1,2,3,4,5])    #得到字符串像是的列表      "[1,2,3,4,5]"
# print( result2 )
#
# result2 = str((1,2,3,4,5))   #支持元组
# print( result2 )
#
# result2 = str(  {"name":"xiaoing"}  )   #支持字典
# print( result2 )
#
# result2 = str(  {"a","b","c","d"}  )   #支持集合
# print( result2 )
#
# #字符串转数字
# print( int("100") )
#
# #字符串转列表
# print( list("hello") )   #将字符串拆成每个字符串组成的列表
#                          #根据这个特点,可以对字符串的字母进行排序
#
# #字符串转元组
# print( tuple("hello") )
#
# #字符串转字典.
# # print( dict(  "hello")  )   #不支持
# print( dict(  hello=100 ) )   #支持使用等于号连接的形式
#
# #字符串转集合
# print( set("hello") )


#eval()  #将参数字符串当做代码来执行.  或者叫做当做表达式来执行

# print( eval("123") )
# print( type(eval("123")) )  #数字类型的123
#
# print( eval("+100") )   #100
# print( eval("-100") )   #-100
#
# # print( int("12+3") )  #错误
# print( eval("12+3") )  #15
# print( eval("12-3") )  #9

# print( int("abc123") )   #错误
# print(  eval("abc123") )   #错误,变量未定义

# center:  让字符串居中,左右填充自定字符
#
# str1 = "hello"
# print( str1.center(10) )    #字符串总共有10位,str1需要居中,左右默认填充空格
# print( str1.center(10,"*") )  #第二参数代表使用什么字符填充
#
# # l代表left.  ljust,字符串左对齐.长度为10位,右侧填充指定字符
# print( str1.ljust(10,"*") )
# print(str1.ljust(10,"*"))
#
# # r代表right.  rjust,字符串右对齐.长度为10位,左侧填充指定字符
# print( str1.rjust(10,"*") )
# print(str1.rjust(10,"*"))
#
#
# #z代表zero    字符串右对齐,长度为10位,左侧填充0
# print( str1.zfill(10))      #左侧填0
# print(str1.zfill(10))
#
# print( str1.ljust(10,"0") )  #右侧填0
# print(str1.ljust(10,"0"))


# find : 在字符串寻找子串是否存在.如果存在则返回下标(0以上的整数),如果不存在,则返回-1

str1 = "today is a good day"
# print(  str1.find("o")  )        #find 默认返回第一次找打的元素下标
# print(  str1.find("o",9,1000)  ) #指定从第9个下标开始寻找
# print(  str1.find( "good" ) )    #子串必须和父串中的元素完全匹配
# print(  str1.find( "z" ) )      #找不到返回-1
# print(str1.find('o'))

#从右到左进行查找,返回的下标依然从左开始数
# print( str1.rfind("good"))
# print( str1.rfind("a",14,15))   #指定区间
# print( str1.rfind("a",-15,-4))#区间同样支持负数
#
# #index和find一样,也是寻找子串位置.但是index找不到会崩溃
# print( str1.index("o") )
# print(str1.index('o',10,15))
# #print( str1.index("z") )  #子字符串没有被找到,崩溃
#
# #从右到左寻找,找不到崩溃,找到返回下标
# print( str1.rindex("a") )
# # print( str1.rindex("nice") )  #不存在,崩溃
#
# print( max(str1) )   #实际上比较的asc码
# print( min(str1) )   #实际上比较的asc码

# # strip() 移除两头指定的字符
# str1 = "****hello****world*****"
# print( str1.strip("*") )    #移除两个头的*
#
# str2 = "        hello    world           "
# print( str2.strip(" ") )   #移除两头的空格
#
# #删除左侧的*
# print( str1.lstrip("*") )
#
# #删除右侧的*
# print( str1.rstrip("*") )

# split  将字符串以某个特定的字符进分割,返回一个列表
# str1 = "today is a good day"
# result = str1.split(" ")    #以空格切分字符串
# print(result)
#
# str2 = "a-b-c-d"
# result = str2.split("-")
# result = str2.split('-')
# print(result)
#
# result = str2.split("-",2)  #使用最多切割次数
# print(result)
#
# result = str2.rsplit("-",2)  #从右侧开始切割,使用次数
# print(result)
#
# str3 = '''hello
# world
# 123
# '''
# # 按照换行符(\n)来进行切割
# print(result)
# result = str3.splitlines()
#
# #如果参数为True,则代表留下这个末尾换行符
# result = str3.splitlines(True)
# print(result)
#
# #拼接  join     将可迭代对象使用某个字符进行连接
# # iterable    可迭代对象: 能够使用for in进行遍历的对象.   str,list,tuple,dict,set
# print( "".join(   ["1","2","","","","","2","2","3","4","5"]  ) ) #list   #用来拼接的列表内的元素,是字符串
# print( "-".join(   ("1","2","3","4","5")  ) ) #tuple
# print( "-".join(   {"1","2","3","4","5"}  ) ) #set
# print( "-".join(   "hello" ) )                #str
# print( "-".join(   {"name":"xiaoming","age":20} ) )   #dict
#
#
# # 切割和拼接就是相对的操作
# #需要将字符串  a:b:c:d  中的 : 改成 -
# str4 = "a:b:c:d"
#
# # 使用系统函数
# # list1 = str4.split(":")
# # print( "-".join(list1) )
#
# #自己实现
# result = ""   #因为字符串自己无法被修改,所以定义另外一个字符串来接接受
# for item in str4:
#     #不等于这个符号,就原样加入新字符
#     if item != ":":
#         result += item
#     else:
#         # 如果等于,就替换成-
#         result += "-"
# print(result)

# replace(old,new,maxCount) 使用new替换old,还可以指定替换次数
#
# str1 = 'this is a test test test'
# print(str1.replace('test','name',2))
# print(str1.replace('name','test',2))
#
# table = str.maketrans('hel','123')
# print(table)
# str2 = 'hello'
# str3 = str2.translate(table)
# print(str3)
# replace(old,new,maxCount)  使用new替换old,还可以指定替换次数

# str1 = "this is a test test test"
#
# print( str1.replace("test","exam") )   #不带次数,则替换所有
# print( str1.replace( "test","exam",2 ) )  #替换两次
#
# # translate  翻译
# # str.maketrans()  创建一个翻译表.   字符串映射表
# table = str.maketrans("hlo","123")   #h->1  l->2  o->3
#
# #这个table,是一个字典.  里面存有字符的映射
# print( table )
#
# #使用这个映射表进行翻译
# str2 = "hello"
# str3 = str2.translate(table)   #使用映射表翻译字符串
# print(str3)
#
# #使用这个映射表,可以做简单的加密.  原理是通过asc码的映射

# 如果字符串全部为字母,并且至少有一个,返回真,其余返回假
# print(   "hello".isalpha()  )   #True
# print(   "hello123".isalpha()  )   #False
# print(   "".isalpha()  )   #False
# print(   "Ab".isalpha()  )   #False

#如果字符串是由字母数字组成,且为一个以上,返回真.否则返回假
# print( "".isalnum() )    #False
# print( "abc".isalnum() )    #True
# print( "123".isalnum() )    #True
# print( "abc123".isalnum() )    #True
# print( "abc123~!@#".isalnum() )    #False

# 字符由大写字母组成,且一个以上.还可以由非小写字母,返回真.
#  如果有小写字母,就返回假
# print( "".isupper() )  #False
# print( "A!@#1231".isupper() ) #True
# print( "a".isupper() )  #False

# 除了大写字母,都返回真
# print( "A".islower() )           #False
# print( "abc123!@#$".islower() )  #True

#如果每个单词首字母大写,返回真
# print( "Hello World".istitle() )   #True
# print( "Hello world".istitle() )   #False

#全部由数字组成,返回真
print( "123.3".isdigit() )    #True
print( "123abc".isdigit() ) #False
print( "!@$#".isdigit() )   #False


str1 = "hello world"
#直接判断字符串是不是以某个字符开头
# print( str1.startswith("h") )    #True
# print( str1.startswith("hello") ) #True
# print( str1.startswith("e") )     #False

#选定区间,再来判断是否以某个字符串开头
# print( str1.startswith("w",6,100) ) #True

#判断是不是以一个字符串结尾
print( str1.endswith("d") )
print( str1.endswith("world") )

#选定区间,再来判断是否以某个字符串结尾
print( str1.endswith("o",0,5)  )


# 因为python对中文支持不是特别好,所以需要进行编解码来处理中文

str1 = "你好 hello  千锋"
print(   str1.encode()  )   #默认使用utf-8进行编码,返回一个二进制的字节(bytes)对象
print(   str1.encode("utf-8")  )  #使用特定的编码格式编码
print(   str1.encode("gbk")  )    #使用特定的编码格式编码

# 默认使用utf-8进行解码   由bytes对象,转成字符串对象
print( b'\xe4\xbd\xa0\xe5\xa5\xbd hello  \xe5\x8d\x83\xe9\x94\x8b'.decode()  )
print( b'\xe4\xbd\xa0\xe5\xa5\xbd hello  \xe5\x8d\x83\xe9\x94\x8b'.decode("utf-8")  )
print( b'\xc4\xe3\xba\xc3 hello  \xc7\xa7\xb7\xe6'.decode("gbk")  )

# 字节对象:bytes.
# 其实计算机的字符串,底层都要转成字节型传输
# print( type(b'\xc4\xe3\xba\xc3 hello  \xc7\xa7\xb7\xe6') )


#获取字符串的asc码
# print( ord("A"))    #65
# print( ord("a"))    #97
# print( ord("0"))    #48

#由asc码获取字符
# print( chr(65) )  #A
# print( chr(97) )  #a
# print( chr(48) )  #字符串0

#不成立  一个是数字0,一个是字符串0
# print( 0 == "0")


#练习:  把 "hello world123"  转成大写
str1 = "hello world123"
new_str = ""
for char in str1:
    #获取字符的asc码
    code = ord(char)

    #如果是小写字母,才进行转换.如果不是,就原样拼接
    if  97<=code<=122:   #   a~z满足要求
        #减去32,即由小写转大写
        result = chr(code-32)
        #把结果拼到新字符串中
        new_str += result
    else:
        new_str += char
print( new_str )

#需求1：统计下面字符串中每个单词的出现次数，并生成一个字典，单词为key，次数为value
str1 = "hello world today is a good day hello world"

#1.将这个字符串拆成单词列表
list1 = str1.split(" ")
print( list1 )

dict1 = {}
for item in list1:
    dict1[item] = list1.count(item)   #dict1["hello"] = list1.count("hello")

print( dict1 )
#不能直接遍历字符串,因为拿到的是每个字母
# for char in str1:
#     print(char)

#需求2：从控制台输入一个字符串，表示时间，编写程序，获取这个时间的下一秒
#例如输入：12:23:33    输出12:23:34

time = input("请输入时间:")

#1.需要将事件进行拆分,得到时分秒
list1 = time.split(":")

#使用input接受过来的数据都是字符,需要转数字
hour = int(  list1[0]  )
minute = int( list1[1]  )
second = int( list1[2]  )

second += 1
if second == 60:
    #秒归零   分钟进位
    second = 0
    minute += 1
    if minute == 60:
        #分钟归零,小时进位
        minute = 0
        hour +=1
        if hour == 24:
            #小时归零
            hour = 0

#%02d   整数有两位,不足两位补0
#%.2d   和上面功能一致
print( "%.2d:%.2d:%.2d"%(hour,minute,second) )

#商品列表
goods_list = [
    ("macBook",10000),
    ("iphoneX",8000),
    ("huawei",4000),
    ("xiaomi",2000),
]
#购物车
shopping_car = []
#余额
money = input("请输入金钱:")
#确保输入的金钱有效
if money.isdigit():
    #将这个金钱转成数字
    money = int(money)

    #因为购物操作可以进行多次,所以使用一个死循环.
    #这里使用死循环的原因是:根本无法得知循环进行多少次.所以只能使用死循环,加break,由用户决定自己退出
    while True:
        #显示商品列表.   下标,元组
        print( "商品列表------------------")
        for index,item in enumerate(goods_list):
            print(index,item)
        print("当前可用余额:",money)
        print("------------------")

        #商品显示完了,需要用户选择了
        choice = input("请选择商品编号,或则输入q退出:")

        #如果是数字,则代表选择了商品编号
        if choice.isdigit():
            # 转数字
            choice = int(choice)
            #商品编号合格
            if 0<=choice< len(goods_list):
                #通过商品编号(下标),获取一个元组
                goods = goods_list[choice]

                #余额大于商品价格,可以进行购买
                #goods[1]  元组中的第1个元素,就是价格
                if money >= goods[1]:
                    #将商品放入购物车
                    shopping_car.append(goods)
                    #将余额减去商品价格
                    money -= goods[1]
                else:
                    print("穷逼,余额不足")
            else:
                print("输入商品编号错误")
        elif choice == "q":
            #显示购物车的内容和余额
            for item in shopping_car:
                print(item)
            print("购物后,还剩余额:",money)
            #退出循环,使用break
            break
        else:
            print("输入商品编号或q错误")
else:
    print( "输入金钱错误" )

