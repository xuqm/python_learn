# coding=utf-8
"""
python中的变量不需要声明
每个变量在使用前必须赋值
变量赋值之后才会被创建

python中变量就是变量，没有类型
我们所说的类型是变量所指的内存中对象的类型
"""
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "xuqm"  # 字符串

"""
python允许同时为多个变量赋值
"""
a = b = c = 1
"""
多个对象指定多个变量
"""
d, e, f = 1.1, True, "3"

"""
python3中有六个标准数据类型
Number(数字)
String(字符串)
List(列表)
Tuple(元组)
Set(集合)
Dictionary(字典)
"""

"""
不可变数据(3个)：Number(数字)、String(字符串)、Tuple(元组)
可变数据(3个):List(列表)、Set(集合)、Dictionary(字典)
"""

"""
内置的type()函数可以用来查询变量所指的对象类型
isinstance()函数可以判断所属类型

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""
print(type(a), type(b), type(c), type(d), type(e), type(f))
print(isinstance(a, int))


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A),  # True
      type(A()) == A,  # True
      isinstance(B(), A),  # True
      type(B()) == A)  # False
"""
数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
"""