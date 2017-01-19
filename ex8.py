formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # %r print this no matter what
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) 
print formatter % (formatter, formatter, formatter, formatter) # how to put formatter inside a formatter
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # The output of this line uses double-quotes 
	"So I said goodnight." # While the output of this line uese single-quotes
) # Becuase "But it didn't sing." contains a ', to make a different from ', the output has to use "".
# Python is to print the strings in the most efficient way it can, not replicate exactly the way you wrote them.