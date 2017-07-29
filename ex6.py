# -*- coding: utf-8 -*-
#定义了x字符串，里面用到一个格式化字符
x = "There are %d types of people." % 10
#定义binary和do_not
binary = "binary"
do_not = "don't"
#运用两个式化字符定义y
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
#'%s'，单引号没有打印出来
print "I also said: '%s'." % y 

#定义变量，格式化字符和变量名可以分开定义，最后打印时再放到一块
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
print w , e