from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
# by f.seek(0) you're moving to the start of the file
# The reason why we use seek here
# because you can only use File.read() or file.readlines() once per file opening.

def rewind(f):
    f.seek(0)
# by f.readline() you're reading a line from the file
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print"First let's print the whole file:\n"
#  print open(input_file).read()
print_all(current_file)

print"Now let's rewind, kind of like a tape."
# print open(input_file).seek(0)
rewind(current_file)

print"Let's print three lines:"
# print line_count = current_line = 1
# print open(input_file).readline()
current_line = 1
print_a_line(current_line, current_file)
# print line_count = current_line + 1 = 2
current_line = current_line + 1
print_a_line(current_line, current_file)
# print line_count = 3
current_line = current_line + 1
print_a_line(current_line, current_file)

