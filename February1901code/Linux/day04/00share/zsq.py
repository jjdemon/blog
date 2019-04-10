

# def say_hello():
#     print "hello!"

# def say_goodbye():
#     print("hello!" ) # bug here
#
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()

#
# def say_hello():
#     print ("[DEBUG]: enter say_hello()")
#     print ("hello!")
#
# def say_goodbye():
#     print ("[DEBUG]: enter say_goodbye()")
#     print ("hello!")
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()



# def debug(func):
#     def wrapper():
#         print("[DEBUG]: enter {}()".format(func.__name__))
#         return func()
#     return wrapper
#
# def say_hello():
#     print ("hello!")
#
# say_hello = debug(say_hello)  # 添加功能并保持原函数名不变
# say_hello()


#
# def debug():
#     import inspect
#     # 获取当前运行的类名函数名
#     caller_name = inspect.stack()[1][3]
#     print ("[DEBUG]: enter {}()".format(caller_name))
#
# def say_hello():
#     debug()
#     print ("hello!")
#
# def say_goodbye():
#     debug()
#     print ("goodbye!")
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()


# how
#
# def debug(func):
#     def wrapper(something):  # 指定一毛一样的参数
#         print ("[DEBUG]: enter {}()".format(func.__name__))
#         return func(something)
#     return wrapper  # 返回包装过函数
#
# @debug
# def say(something):
#     print ("hello {}!".format(something))
#
#
# say('world')



# def debug(func):
#     def wrapper(*args, **kwargs):  # 可变参数关键字参数
#         print ("[DEBUG]: enter {}()".format(func.__name__))
#         print ('Prepare and say...')
#         return func(*args, **kwargs)
#     return wrapper  # 返回
#
# @debug
# def say(something):
#     print ("hello {}!".format(something))
#
#
# say('hello,')

# 高级一点的装饰器
# def logging(level):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             print( "[{level}]: enter function {func}()".format(
#                 level=level,
#                 func=func.__name__))
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return wrapper

# 当带参数的装饰器被打在某个函数上时，比如@logging(level='DEBUG')，它其实是一个函数，会马上被执行
# @logging(level='INFO')
# def say(something):
    # print ("say {}!".format(something))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)
#
#
# say('hello')



# @logging(level='DEBUG')
# def do(something):
#     print "do {}...".format(something)
#
# if __name__ == '__main__':
#     say('hello')
#     do("my work")


# 基于类实现的装饰器
#
# 装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，
# 		然后返回一个callable对象。在Python中一般callable对象都是函数，但也有例外。
# 		只要某个对象重载了__call__()方法，那么这个对象就是callable的。
# # class logging(object):
#	  
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print ("[DEBUG]: enter function {func}()".format(
#             func=self.func.__name__))
#         return self.func(*args, **kwargs)

# # @logging
# def say(something):
#     print ("say {}!".format(something))
#
# say = logging(say)
#	
# 