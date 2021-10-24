course = 'Python for Beginners'
# using a function/method with strings
print(course.upper())  # returns a new string in CAPS
print(course.find('P'))  # finds the index of a character
print(course.replace('for', '4'))  # replace the string for with string 4
print('Python' in course)  # checking to see if the word(string) in exist in course, this will return a boolean value

# ----------------------------
# ARITHMETIC operations
# ----------------------------

print(10 + 3)  # addition(+), subtract(-), division with floating point number(/)with whole no (//), multiplication(*)
print(10 % 3)  # remainder of a division
print(10 ** 3)  # addition exponent, that is raised to the power of

# augmented assignment operator
x = 10
x = x + 3  # normal way
print(x)
x += 3  # augmented assignment operator used - *=, -=
print(x)

# just like in maths, operator precedence multiplication before addition
y = 10 + 3 * 2  # this will give 16, 3 * 2 before adding 10
z = (10 + 3) * 2  # this will give 26 as 10 + 2 will be evaluated first
print(y)
print(z)

# ----------------------------------
# COMPARISON Operators
# ----------------------------------

x = 3 > 2
print(x)  # this will give boolean result True or False
# > - greater than
# < - less than
# <= - less than or equals to
# >= - greater than or equals to
# != not equal to
# == equal to

# ----------------------------------
# LOGICAL Operators - revise the truth table for better knowledge
# ----------------------------------

price = 25
print(price > 10 and price < 30) # T and T = True
print(price > 10 or price < 30)  # T or T = True
print(price > 30 or price < 25)  # F or F = False
print(not price > 30)  # True
