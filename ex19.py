def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
# each time, we pass a set of arguments to the cheese_and_crackers functions
# in this case, 20 and 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# in this case, we create a set of variables 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# in this case, we use () to do calculations
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# in this case, we do math using variables' values
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)