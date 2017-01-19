#Use only script to do it
filename = "Brynaisawesome.txt"

txt = open(filename) 

print "Here's your file %r:" % filename 

print txt.read() 

print "Type the file name agian:"

file_again = "ex15_sample.txt"

txt_again = open(file_again)

print txt_again.read()
