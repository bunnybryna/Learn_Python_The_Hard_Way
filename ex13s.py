from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "What did you have for breakfast?",
breakfast = raw_input()
print "What did you have for lunch?",
lunch = raw_input()
print "What did you have for dinner?",
dinner = raw_input()
print "So, you had %r for breakfast, %r for lunch and %r for dinner. " % (
    breakfast, lunch, dinner)


