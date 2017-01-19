from sys import argv

script, user_name, date = argv
prompt ="*"

print "Hi %s, I'm the %s script." % (user_name, script)
print "Today is %s." % date
print "I'd like to ask you a few questions. "

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of specialty do you have?"
hobby = raw_input(prompt)

print "Who do you love most in the world %s?" % user_name
love = raw_input(prompt)

print "What is your favoroute food in the world %s?" % user_name
food = raw_input(prompt)

print "In %s, %s stated that:" % (date, user_name) 
print """
I live in %r. Not sure where that is.
I can %r.
And I love %r and %r most. Nice.
""" % (lives, hobby, love, food)
