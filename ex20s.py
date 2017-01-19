from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
# by f.seek(0) you're moving to the start of the file
def rewind(f):
    f.seek(0)
# by f.readline() you're reading a line from the file
def print_a_line(line_count, f):
#Each time you do f.readline() you're reading a line from the file
# and moving the read head to right after the \n that ends that line
    print line_count, f.readline()

current_file = open(input_file)

print"First let's print the whole file:\n"
#  print open(input_file).read()
print_all(current_file)

print"Now let's rewind, kind of like a tape."
# print open(input_file).seek(0)
rewind(current_file)

print"Let's print three lines:"

# redo it with a contraction, x = x + y is the same as x += y
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
