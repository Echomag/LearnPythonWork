# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

#定义了一个函数：输出文件的所有内容到屏幕
def print_all(f):
	print f.read()
	
#定义了一个函数，seek() 方法用于移动文件读取指针到指定位置。f.seek(0)重新设置文件读取指针到开头
def rewind(f):
	f.seek(0)
	
#定义函数，输出行号和该行的内容
def print_a_line(line_count, f):
	print line_count, f.readline(),

#打开import的文件，给变量current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

#使用函数print_all打印current_file内容到屏幕
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#因为打印完，重新让文件读取指针到开头，这样过会f.readline才会从第一行开始
rewind(current_file)

print "Let's print three lines:"

#输出第一行
current_line = 1
print_a_line(current_line, current_file)

#输出第二行
current_line += 1
print_a_line(current_line, current_file)

#输出第三行
current_line += 1
print_a_line(current_line, current_file)