
# Use only raw_input to do it
print "Type a file name:"
filename = raw_input("^^^")
txt = open(filename)

print "Here's your file %r:" % filename 
print txt.read()

print "Type another file name:"
another_file = raw_input("***")
txt_another = open(another_file)
print txt_another.read()

