# you can pass in two arguments to change the range and iteration variable
def wloop(a,b):
	i = 0
	numbers = []
	# variablize everything, replace 6 with a
	while i < a:
		#print "At the top i is %d" % i
		numbers.append(i)
		# replace 1 with b
		i = i + b
		#print "Numbers now: ", numbers
		#print "At the bottom i is %d" % i
		print "The numbers:", numbers
	for num in numbers:
		print num,
		
# rewrite the function with a for-loop and range 
def floop(a):
	# remember to put the empty list out of the for loop
	# or you will only get the last element of the increment [5]and[9]
	numbers = []
	for i in range(0,a):	
		numbers.append(i)
	print "The numbers:", numbers
	for num in numbers:
		print num,

wloop(6,1) 
print "\n"
wloop(10,2)
print "\n"
floop(6)
print "\n"
floop(10)