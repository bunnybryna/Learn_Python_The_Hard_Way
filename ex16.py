from sys import argv
# python ex16.py test.txt, rememer to give the argument to the command line
script, filename = argv

print "We're going to erase %r." % filename
# CTRL-C is just a string. Since you will choose "want that" and hit return, the program just go on.
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# Just hit Return/enter to continue, no trick.
raw_input("?")

print "Opening the file..."
# target is a variable you name, open(name[,mode[,buffering]])
# w is an extra parameter to open, means open the file in write mode, r for read and a for append, r is the default mode
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()