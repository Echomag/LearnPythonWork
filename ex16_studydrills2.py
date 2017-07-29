from sys import argv

script , filename = argv

fo = open(filename, 'r+')
line1 = fo.readline()
line2 = fo.readline()
line3 = fo.readline()

print "first line ", line1,
print "second line ", line2,
print "third line ", line3,