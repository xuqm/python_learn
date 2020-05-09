# coding=utf-8
# -*- coding:utf-8 -*-

"""
以上是指定编码格式的方法
"""

"""
关于注释：多行注释使用三重双引号
单号注释使用 #
"""
print("Hello World!")

"""
python 使用缩进来表示代码块
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
"""
# 这个例子，else无法进入
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print(False)

"""
如果语句过长，无法一行写完，可以使用反斜线 \
"""
total = "item_one" + \
        "item_two" + \
        "item_three"

"""
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
"""
total = ['item_one', 'item_two', 'item_three', 'item_four', 'item_five', ]

"""
python 中有的数字有四种类型 
int(整数) 没有long
bool(布尔) True
float(浮点) 1.23 3E-2
complex(复数) 1+2j 1.1+2.2j
"""
print(3E-2)  # 3乘10的-2次方
print(2 ** -2)  # ** 幂运算
print(3 ** -2)

"""
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
"""
string = 'Runoob'

print(string)  # 输出字符串
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符
print(string[0])  # 输出字符串第一个字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string[2:])  # 输出从第三个开始后的所有字符
print(string * 2)  # 输出字符串两次
print(string + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

"""
空行与代码缩进不同，空行并不是Python语法的一部分。
书写时不插入空行，Python解释器运行也不会出错。
但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构
"""

"""
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
"""
import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

"""
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
"""
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")

'''
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

"""
Python可以使用-h参数查看各参数帮助信息
"""