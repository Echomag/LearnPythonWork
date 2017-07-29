## -*- coding: utf-8 -*-
from sys import argv

script, filename = argv


print "We're going to erase %r." % filename 
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')  # 以写入模式打开文件，后面可以执行清空操作
 
print "Truncating the file. Goodbye!"
#target.truncate()             #清空文件

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."


#一行一行的以追加的形式写入到文件里
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

