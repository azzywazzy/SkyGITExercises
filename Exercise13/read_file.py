# opens file and reads it all
pelican = open("pelican.txt", "r")
reading = pelican.read()

# prints the file contents, each line broken out - variable currently returned as a string
print(type(reading))
print(reading)

# code that will read the file into a list and print out the number of items/lines in the list
lines = open("pelican.txt").readlines()
print(len(lines))

# use a loop to iterate over and print the file contents, not including any blanks
for line in open("pelican.txt"):
    print(line, end="")
