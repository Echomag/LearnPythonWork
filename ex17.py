## -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#把文件from_file打开赋给左边的变量，返回的不是文件内容，是一个叫做file object的东西
in_file = open(from_file) 

#把in_file的内容给变量indata
indata = in_file.read()

#返回字符串长度
print "The input file is %d bytes long" % len(indata) 

#存在文件返回True否则False
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()