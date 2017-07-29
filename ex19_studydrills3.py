# -*- coding: utf-8 -*-
def are_you_fat(weight, height):
	print "You are %d meters tall, and  %d kilograms weight." % (height, weight)
	print "Your normal weight is %d." % (height-100)
	

#1
are_you_fat(50.0, 160.0)
print 

#2
S_height = 170
S_weight = 79
are_you_fat(S_weight, S_height)

#3
S_height = 170
S_weight = 79
are_you_fat(S_weight + 20, S_height -15)

#4
are_you_fat(2*60, 6*14)

#5  尽量避免使用和函数一样的变量名
weight = int(raw_input("Input your weight: "))
height = int(raw_input("Input your height: "))

are_you_fat(weight, height)

#6
s_height = 170
s_weight = int(raw_input("Input your weight: "))
are_you_fat(s_weight, s_height)

#7
S_height = 170
are_you_fat(10*9, s_height)

#8
S_height = 170
are_you_fat(50, s_height+18)

#9  
s_weight = int(raw_input("Input your weight: "))
s_height = int(raw_input("Input your height: "))

are_you_fat(s_weight-10, s_height-10)

#10  
s_weight = int(raw_input("Input your weight: "))
s_height = int(raw_input("Input your height: "))

s_weight2 = s_weight + 10
s_height2 = s_height + 10
are_you_fat(s_weight2, s_height2)