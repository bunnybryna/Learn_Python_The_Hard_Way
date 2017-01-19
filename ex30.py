people = 30
cars = 40
trucks = 15

# 40>30, this will run
if cars > people:
    print "We should take cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
# 15<40, this will run
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
# 30>15, this will run
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
