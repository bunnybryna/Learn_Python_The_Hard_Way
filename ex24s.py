
def get_fn(start):
	a = 20 + start
	b = 50 + a
	c = 90 + b
	return a, b, c

start = 20
e,f,g = get_fn(start)
print start
print e,f,g
print "We have a as %d, b as %d, c as %d." % (e,f,g)
print "We have a as %d, b as %d, c as %d." % get_fn(start)


