# this one is like your scripts with argv
# * is to take all the arguments to the function and then put them in args as a list. 
# it is not normally used too often unless specifically needed.
def print_two(*args):
    # indentation, four spaces is the best!
    print "args: %r" %(args,)
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2, arg3):
    print "arg1: %r, arg2: %r" %(arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    print print_two_again("1", "2", "3")

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw", "Test")
print_one("First!")
print_none()	