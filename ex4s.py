cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
# cars_not_driven = 100 - 30 = 70
cars_not_driven = cars - drivers
# cars_driven = 30
cars_driven = drivers
# carpool_capacity = 30 * 4 = 120
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = 90 / 30 = 3
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."