# -*- coding: utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses." % cheese_count
	print "You have %d boxes 0f crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	

#直接给函数数值	
print "We can just give the function numbers directly;"
cheese_and_crackers(20, 30)

#函数的参数也可以用变量先设置在使用
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#函数参数可以用数学计算式输入
print "We can even do matn inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#使用变量和数值输入函数参数
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)