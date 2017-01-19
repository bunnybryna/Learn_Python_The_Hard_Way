print "Where do you live ?" 
lives = raw_input(prompt)

print "What kind of specialty do you have?"
specialty = raw_input(prompt)

print "Who do you love most in the world ?" 
love = raw_input(prompt)

print "What is your favoroute food in the world?" 
food = raw_input(prompt)

print """
I live in %r. Not sure where that is.
I can %r.
And I love %r and %r most. Nice.
""" % (lives, specialty, love, food)
