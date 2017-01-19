# this program is to show how funcitons and arguments work together
def superbowl():
    def wings_and_beer(wings, cans_of_beer):
        print "You have %d chicken wings!" % wings
        print "You have %d cans of beer!" % cans_of_beer
        print "Oh, yeah, that's enough!"
        print "Super Bowl is on!!!\n"

# each time, we pass a set of arguments to the cheese_and_crackers functions
# 1st run, the arguments are 30 & 24, u can print out the arguments to debug	
print "How to give functions the values it needs to print them: "
print "First, we can pass straight numbers to the function: "
wings_and_beer(30, 24)

# 2nd run, we create a set of variablesthe wings_num & beer_num and assign the value of 20 & 12 to them
print "Or, we can declare variables in the script: "
# Note that we name the varaibles different from the main argument "wings" to avoid the confusion
wings_num = 20
beer_num = 12
wings_and_beer(wings_num, beer_num)	

# 3rd run we do  math 
print "Also, We can even do math inside the parentheses: "
wings_and_beer(30 + 20, 24 + 12)

# 4th run, we add variables and numbers together
print "Besides, we can combine variables and calculations: "
wings_and_beer(wings_num + 100, beer_num + 120)

# 5th run, let the user input anything
print "Now, let's be more interactive."
print "Please enter the number of chicken wings and cans of beer you prepare for the super bowl."
amount_of_wings = raw_input ("How many chicken wings?")
amount_of_beer = raw_input ("How many cans of beer?")
wings_and_beer(int(amount_of_wings), int(amount_of_beer))


	
