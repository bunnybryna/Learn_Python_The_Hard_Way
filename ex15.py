#Tell you where you can get your arguments
from sys import argv 
# You need to give two arguments in the command line, one is your script name, the other is the txt file you want to open
script, filename = argv 
# Using open command to open a file, put the argument filename in the () 
txt = open(filename) 
# Remind you that your file is shown as below
print "Here's your file %r:" % filename 
# Print the variable txt for you like hey txt, read it with no parameters, () means no parameters
print txt.read() # 
# Try again with the same name
print "Type the file name agian:"
# Using raw_input to get the file name
file_again = raw_input(">")
# Using open command to open the file
txt_again = open(file_again)
# Read it again with no parameters
print txt_again.read()
