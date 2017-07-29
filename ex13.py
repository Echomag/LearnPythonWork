from sys import argv
#import a module named argv=argument variables,and argv hold the argument variables

script, first, second, third = argv
#at this step,unpacking the argv ,assign the argv to the left variables in order

print "The script is called:", script
print "Your first variable is:", first
print "Your second  variable is:", second
print "Your third variable is:", third