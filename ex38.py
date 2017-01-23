ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Nignt", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    #.pop removes and returns the last item
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]

print stuff[-1]

print stuff.pop()
# str.join(sequence) returns a string, which is the concatenation of the strings in the sequence seq, the separator between elements is the string
# will produce Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print ' '.join(stuff)
# will produce Telephone#Light
print '#'.join(stuff[3:5])    