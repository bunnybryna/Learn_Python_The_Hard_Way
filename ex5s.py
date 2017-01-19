name = 'Bryna Zhao'
age = 28 # though I look like 18!
height = 167 # cm
weight = 50 # kg
eyes = 'black'
teeth = 'white'
hair = 'black'

print "Let's talk about %s." % name
print "She's %d centimeters tall." % height
print "She's %d kilograms heavy." % weight
print "Actually that's not too heavy." 
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on her dental health." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)