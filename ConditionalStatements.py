# ----------------------------------
# Conditional Statements - if/else Statements
# ----------------------------------

temperature = 9
if temperature > 30:
    print("it's a hot day")
    print('drink plenty of water')
elif temperature > 20:
    print("it's a nice day")
elif temperature > 10:
    print("it's a cold day")
else:
    print("it's freezing")
print("Done")

# get an input and try out an if statement with a comparison operator
a = int(input("Enter a number: "))

b = 8

if a < b:
    print(str(a) + ' is less than ' + str(b))
