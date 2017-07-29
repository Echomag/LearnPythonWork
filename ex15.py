from sys import argv

script, filename = argv
#assign the contents of the file named  filename to a variales named txt
txt = open(filename)

print "Here's yor file %r:" % filename

#directly output the contents of the txt
print txt.read()

#through user input to get the new file name
print "Type the filename again:"
file_again = raw_input("> ")

#assign the contents of the file input right now to a variales named txt_again
txt_again = open(file_again)

#print txt_again content
print txt_again.read()

txt.close()
txt_again.close()