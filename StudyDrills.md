# 《笨办法学Python》附加思考

---
[TOC]

---
#ex1
1,
```
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

print 'Another line'
```
2, 
```
#print "Hello World!"
#print "Hello Again"
#print "I like typing this."
#print "This is fun."
#print 'Yay! Printing.'
#print "I'd much rather you 'not'."
#print 'I "said" do not touch this.'

print 'Just print one line'
```
3, `#`是做注释用的，`#`以后的内容会被python忽略，可以写自己的理解，或是写说明让别人明白这是做什么的代码,或是禁用某句代码。

#ex2
1, 同上

#ex3
1, 见 ex3.py
2, 把python当计算器用
```
PS C:\Users\py> python
Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 7/4
1
>>> 7.0/4
1.75
>>> 0-4
-4
>>> 1+2,1/2, 9-8
(3, 0, 1)
```
3, 见 ex3_studydrills3.py
```
print "Let me count how much money I paid this month."
print "For food: ", 20 + 30 + 40 + 50 + 200
print "For living stuff: ", 400*0.8 + 200
print "Totally, ", 20 + 30 + 40 + 50 + 200 + 400*0.8 + 200
```
```
PS C:\Users\py\mystuff> python .\ex3_studydrills3.py
Let me count how much money I paid this month.
For food:  340
For living stuff:  520.0
Totally,  860.0
```
4, 以为浮点数是带小数点的数。搜索浮点数以后，发现这是个庞大的概念，还有国际标准。
在计算机中用以近似表示任意某个实数。具体的说，这个实数由一个整数或定点数（即尾数）乘以某个基数（计算机中通常是2）的整数次幂得到，这种表示方法类似于基数为10的科学计数法。计算机是整型机器, 只有使用复杂的代码才能表示实数。最常用的表示实数的代码称为 IEEE Floating-Point Standard

5, 见 ex3_studydrills5.py

#ex4
第8行里有个变量`car_pool_capacity`没有定义过
1, 只用4的话，计算只显示整数，看到的数值不完整
3, 见ex4.py
6, 
```
Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> i = 30
>>> j =9
>>> h = 10
>>> i +j
39
>>> h-i
-20
>>> j*10
90
```

#ex5
1, 见 ex5_studydrills1.py
3,
格式符为真实值预留位置，并控制显示的格式。格式符可以包含有一个类型码，用以控制显示的类型，如下:
`%s`    字符串 (采用str()的显示)
`%r`    字符串 (采用repr()的显示)
`%c`    单个字符
`%b`    二进制整数
`%d`    十进制整数
`%i`    十进制整数
`%o`    八进制整数
`%x`    十六进制整数
`%e`    指数 (基底写为e)
`%E`    指数 (基底写为E)
`%f`    浮点数
`%F`    浮点数，与上相同
`%g`   指数(e)或浮点数 (根据显示长度)
`%G`    指数(E)或浮点数 (根据显示长度)
4,
```
Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> in1equal_cm = 2.54
>>> lbs1equal_kg = 0.453592
>>> 55 * in1equal_cm
139.7
>>> 90 * lbs1equal_kg
40.82328
```

#ex6
1, 见ex6.py
2, 
```
# -*- coding: utf-8 -*-
#定义了x字符串，里面用到一个格式化字符
x = "There are %d types of people." % 10
#定义binary和do_not
binary = "binary"
do_not = "don't"
#运用两个式化字符定义y
y = "Those who know %s and those who %s." %(binary, do_not) # 1

print x
print y

print "I said: %r." % x # 2
#'%s'，单引号没有打印出来
print "I also said: '%s'." % y  # 3

#定义变量，格式化字符和变量名可以分开定义，最后打印时再放到一块
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # 4

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
```
3, 确定，是4个
4, 因为他们是字符串。用`,`相连中间会加个空格

#ex7
1, 见ex7.py
3, 好主意！记录自己犯过的错误
4, 不要重复采坑！
5, 每个人都会犯错。

#ex8
2, `''` `""`都是python识别字符串的标识符，都是一样的。


#ex9
养成记录犯错的习惯，不要再犯

#ex10
1,转义字符
`\\`	Backslash (\) 反斜杠
`\'`	Single-quote (') 单引号
`\"`	Double-quote (") 双引号
`\a`	ASCII bell (BEL)  ASCII响铃符
`\b`	ASCII backspace (BS)  ASCII退格键
`\f`	ASCII formfeed (FF)  ASCII进纸键
`\n`	ASCII linefeed (LF)  ASCII换行符
`\N{name}`	Character named name in the Unicode database (Unicode only)；Unicode数据库中的字符名，name是他的名字，仅适用于Unicode
`\r`	Carriage Return (CR)  ASCII回车符
`\t`	Horizontal Tab (TAB) 水平制表符
`\v`	ASCII vertical tab (VT)  ASCII垂直制表符
`\uxxxx`	Character with 16-bit hex value xxxx (u'' string only)；值为16位十六进制值xxxx的字符
`\Uxxxxxxxx`	Character with 32-bit hex value xxxxxxxx (u'' string only) ；值为32位十六进制值xxxxxxxx的字符
`\ooo`	Character with octal value ooo 值为八进制ooo的字符
`\xhh`	Character with hex value hh 值为十六进制数hh的字符

2,是一样的，
3,
```
print "\tHey man,I know your name is %s,\n\tand you come fron %s.\n\tYou live here for %d years." % ("Zed", "Tianjin", 5)
```
输出
```
        Hey man,I know your name is Zed,
        and you come fron Tianjin.
        You live here for 5 years
```
4,使用`%r`打印的是写在脚本里的东西
```
print """
\tHey man,I know your name is %s,
\tHey man,I know your name is %r again,
\tand you come fron %r.
\tYou live here for %r years." 
""" % ("Zed", "Zed", "Tianjin", 5)
```
输出
```
        Hey man,I know your name is Zed,
        Hey man,I know your name is 'Zed' again,
        and you come fron 'Tianjin'.
        You live here for 5 years."
```


#ex11
1, 通过读取控制台的输入与用户实现交互。可以输入字符串、数值，对数值型可进行取整`int(raw_input())`和取浮点数`float(raw_input())` 
3, 见 ex11_studydrills3.py

#ex12
1,  
```
PS C:\Users\py> python -m pydoc raw_input #-m 以脚本方式运行模块
Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
```
3,  `pydoc`主要用于从python模块中自动生成文档，这些文档可以基于文本呈现的、也可以生成WEB 页面的，还可以在服务器上以浏览器的方式呈现！
4, `open` This is prefered way to open a file
    `file` open file, prefered use with open
    `os`   export
    `sys`  access to some objects argv
    
#ex13
1, argv解包时定义了三个变量，同样需要在运行脚本时提供3个变量
```
PS C:\Users\py\mystuff> python ex13.py first 2nd
Traceback (most recent call last):
  File "ex13.py", line 4, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack
```
2, 见 ex13_studydrills2_1.py ex13_studydrills2_2.py
3, 见 ex13_studydrills3.py

#ex14
2, 改成了`prompt = "Please enter the answer:  "`
3, 见ex14_studydrills3.py

#ex15
1, 见ex15.py
4, 打印了文件
```
PS C:\Users\py\mystuff> python .\ex15_studydrills4.py ex15_sample.txt
Here's yor file 'ex15_sample.txt':
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```
5, 用命令行会更好，可以直接运行，不用中途停下来等待输入
6,7,
```
Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> txt = open("ex15_sample.txt")
>>> print txt.read()
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
>>> print txt.readline() #文件内容运行过一次就的重新加载

>>> txt = open("ex15_sample.txt")
>>> print txt.readline()
This is stuff I typed into a file.

>>> filename = "ex15_sample.txt"
>>> txt_again =open(filename)
>>> txt_again.readlines() #可以不加print也能显示
['This is stuff I typed into a file.\n', 'It is really cool stuff.\n', 'Lots and lots of fun to have in here.']
>>> txt_again =open(filename)
>>> print txt_again.readlines()
['This is stuff I typed into a file.\n', 'It is really cool stuff.\n', 'Lots and lots of fun to have in here.']
```
8, 见ex15.py
```
txt.close()
txt_again.close()
```

#ex16
1, 见ex16.py
2, 见ex16_studydrills2.py
3,`target.write("%s\n%s\n%s\n" % (line1, line2, line3))`
4, `w`是写入模式，只有指定以后才能对文件的内容进行更改
5, 用`w`模式打开，不需要用`target.truncate()`清空文件内容，因为`w`会直接覆盖原有文件

#ex17
1, import用来导入模块，有很多已经写好的资源可以调用，用什么调用什么
2,
```
from sys import argv

script, from_file, to_file = argv

print "Coping from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
```
3, 
```
from sys import argv

script, from_file, to_file = argv

in_file = open(from_file); indata = in_file.read()

out_file = open(to_file, 'w'); out_file.write(indata)

out_file.close(); in_file.close()
```
4, 用的windows
5, windows上的powershell可以用`type`打印整个文件
6, 在网上找到一些回答，close()是为了释放资源。如果程序是一个服务，或是需要很长时间才能执行完，或者很大并发执行，就可能导致资源被耗尽，也有可能导致死锁。 

#ex19
1, 见ex19.py
3, 见ex19_studydrills3.py

#ex20
1, 见ex20.py
2, `current_line`初始值为1，第一行直接是定义的行号；
执行`current_line += 1`后，`current_line+1`替代了`current_line`的初始值，此时等于2；
再次执行`current_line += 1`后，在`current_line=2`的基础上+1，此时等于3.
4, seek() 用于移动文件读取指针到指定位置。f.seek(0)重新设置文件读取指针到开头
**语法**
fileObject.seek(offset[, whence])
**参数**
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为0。给offset参数一个定义，表示要从哪个位置开始偏移；**0**代表从文件开头开始算起，**1**代表从当前位置开始算起，**2**代表从文件末尾算起。
5, 
```
>>> a = 1
>>> a += 1 
>>> a
2
>>>a *= 2
>>>a
4
>>>a -= 1
>>>a
3
```
#ex21
2, 
```
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

v1 = divide(iq, 2)
v2 = multiply(weight, v1)
v3 = subtract(height, v2)
what1 = add(age, v3)

print what1, "It's same as", what
```
3,4,
```
def all(a, b, c, d):
	print "a: %d, b: %d, c: %d, d: %d" % (a, b, c, d)
	return (c -((a / 2) * b )) + d
	
reslut = all(2,1,1,1)
print "The reslut is: ", reslut
```
```
The reslut is: 1
```