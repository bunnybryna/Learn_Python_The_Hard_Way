from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how? delete the variable "in_file"
indata = open(from_file).read()
# len() gets the length of the string that you pass to it then returns that as a number 
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
# No need to ask before doing the copy, just delete the line below. 
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# delete the variable "out_file",out_file = open(to_file, 'w')
open(to_file, 'w').write(indata)

print "Alright, all done."

open(to_file).close()
open(from_file).close()
