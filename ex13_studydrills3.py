from sys import argv

script, name1, name2 = argv

print "The first people called:", name1
print "The second people called:", name2

age1 = int(raw_input("How old are you %s? " % name1) )
age2 = int(raw_input("And you, %s? "% name2) )

print "Your total age is %d." % (age1+age2)