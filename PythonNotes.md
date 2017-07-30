# **Python学习笔记**
---
## 软件要做的事
1. 接受人的输入
2. 改变输入的内容
3. 打印出改变了的东西

## 简单操作
- 要使用中文批注，不报ASCII错误，要在首行加入 `# -*- coding: utf-8 -*-`
- 查看文档
```
python raw_input            # Linux
python  -m pydoc raw_input  # Windows
```

- 退出python
```
Ctrl + D                    # Linux
Ctrl + Z                    # Windows
quit()
```

- print
print输出完结果后会自动加上换行符`\n`，如果不需要换行可以加上`,` 就不会输出换行符来结束这一行跑到下面一行去了

- `“ ”` 和`‘ ’`是python识别字符串的标识
```
print “Hello World!” 
print ‘Hello World!’	
print “Hello World!”, 27, “years girl.”

print “Hello World!”, 27, 
print “years girl.”
```
```
Hello World!
Hello World!
Hello World! 27 years girl.

Hello World! 27 years girl.
```
- 定义多行字符串，下例也可以用`"""   """` 或`'''  '''`
```
print """
There's something going on here.
With the three double-quotes."""
```
```
There's something going on here.
With the three double-quotes.
```
- `=`作用是把右边的值赋给左边的变量名，变量名要以字母开头，是字母、数字、下划线的组合，变量是不会有引号的

- `==`的作用是检查左右两边是否相等
`variable1 = 100`
`variable2 = variable1 * 3`

- `x += y` 等同于` x = x + y`，同理 `x -= y`

## 格式化字符串format string
- 为真实值预留位置，并控制显示的格式

- 格式符包含类型码
 `%s` 字符串
 `%d` 十进制整数
 `%f` 浮点数
 `%r`是用来做调试的（debug），会显示变量的原始数据，而`%s`和其他符号则是用来向用户显示输出的
```
print "There are %d types of people." % 10   #一个变量
x = "There are %s types of %s people." % (“three”, “American”) #两个及以上变量的用法
```
- 定义变量，格式化字符和变量名可以分开定义，最后打印时再放到一块
```
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
```
## 接受输入
### 交互式接收输入
```
x = raw_input( )
x = raw_input( "Input your name: ") # 可以提示输入的内容
x = int(raw_input( )) #接受数值用于计算，并将数值取整

prompt = "> "
likes = raw_input(prompt) # 把用户提示符变成一个变量，要是以后要修改成别的字符，只要改一个位置就可以
```

### 从脚本接收输入
`import`导入模块module（或者称为库library）；
`argv`即参数变量argument variable，保存你运行Python脚本时传递给Python脚本的参数。
`python ex13.py first 2nd`
```
from sys import argv          #第一行把sys模块导进来

script, first, second = argv  #第三行是将参数解包unpack，把参数依次赋值给左边的变量
	
print "The script is called:", script
print "Your first variable is:", first
print "Your second  variable is:", second
```

## 文件操作
使用方法 `F.操作`，如`F.close()`, `F.read()`
**`open() -> 中间过程 -> F.close()`**

**open()**
`open(路径+文件名,读写模式)`
- open对于文件的写入态度是安全第一，只有特别指定后，才会进入写入模式
- 读写模式:r只读,r+读写,w写入(会覆盖原有文件),a追加

**read()**	
读取文件内容，可以把结果赋给一个变量
```
fo = open("test.txt")
print fo.read()
```

**readline()**
读取文本文件中的一行,内部过程是会扫描文件的每一个字符，直到找到一个`\n`为止，然后停止读取文件，并且返回此前的文件内容。文件会记录每次调用readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行了。

**seek**
方法用于移动文件读取指针到指定位置。
`fileObject.seek(offset[, whence])`
- 参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

**truncate()**
清空文件，请**小心**使用该命令
truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
runoob.txt
`1:www.runoob.com
2:www.runoob.com
3:www.runoob.com`
```
fo = open("runoob.txt", "r+")

# 截取10个字节
fo.truncate(10)

str = fo.read()
print "读取数据: %s" % (str)

fo.close()
```
结果
```
读取数据: 1:www.runo
```
**write(stuff)**
将stuff写入文件
```
in_file = open("test.txt")
inputdata = in_file.read() #读文件内容到字符串，给变量inputdata,不然无法写入。
out_file = open(to_file, 'w') #out_file.write(in_file)是错误的
out_file.write(inputdata)
```
**close()**
关闭文件

## 函数的定义与使用
1.定义函数
函数可以做很多事情，打印内容，做计算，定义可以用规则去做的事情，下次直接用
```
def peanuts(*argv):
    arg1, arg2 = argv
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#可以直接用参数的名字，而不用解包,参数的个数不限，也可以没有参数
def print_two_again(arg1, arg2 ):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
```
2.函数定义及使用注意事项自检列表
*定义*
- 函数定义是以def开始的吗？
- 函数名是以字符和下划线组成的吗？
- 函数名是不是紧跟着括号`(`?
- 括号里是否包含参数？多个参数是否以逗号隔开？
- 参数名称是否有重复？不能使用重复的参数名
- 紧跟着参数的是不是`):`?
- 紧跟着函数定义的代码是否使用了4个空格的缩进？
- 函数结束的位置是否取消了缩进？

*使用*
- 调用函数时是否使用了函数名？
- 函数名是否紧跟着`(`?
- 括号后有无参数？多个参数是否以逗号隔开？
- 函数是否以`)`结尾？

运行run, 调用call, 使用use是一个意思

3.函数的参数传递方法
- 直接给数字
- 给变量
- 给数学表达
- 数学表达和变量结合用

4.函数的返回值`return`
函数的返回值可以赋给变量

```
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

v1 = add(12,13)
print "Equal: ", v1
```

```
ADDING 12 + 13
Equal: 25
```

## 遇到的报错
- SyntaxError: invalid syntax
```
#错误写法
print "You name is %r, you come from %r." % 
(name, adress)
#正确写法
print "You name is %r, you come from %r. " % (name, adress)
print "You name is %r, you come from %r. " % (
name, adress)
```
- 使用格式化字符参数给少了
```
Traceback (most recent call last):
  File "ex10.py", line 26, in <module>
    """ % ("Zed", "Tianjin", 5)
TypeError: not enough arguments for format string

```




