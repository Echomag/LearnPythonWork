# -*- coding: utf-8 -*-
# This one is like your scripts with argv
#定义函数print_two,名字可以改成其他的，*argv可以指多个变量但不常使用，第二行解包参数
def peanuts(*argv):
    arg1, arg2 = argv
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
#可以直接用参数的名字，而不用解包
def print_two_again(arg1, arg2 ):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument，定义一个参数
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one take no argument
def print_none():
	print "I got nothin'."
	
#调用定义的函数，不同函数的变量名可以相同
peanuts("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()