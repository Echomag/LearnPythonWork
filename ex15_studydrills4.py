from sys import argv

script, filename = argv
#assign the contents of the file named  filename to a variales named txt
txt = open(filename)

print "Here's yor file %r:" % filename
#directly output the contents of the txt
print txt.read()

