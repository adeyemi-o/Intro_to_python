course = 'Python for Beginners'
# using a function/method with strings
print(course.upper())  # returns a new string in CAPS
print(course.find('P'))  # finds the index of a character
print(course.replace('for', '4'))  # replace the string for with string 4
print('Python' in course)  # checking to see if the word(string) in exist in course, this will return a boolean value

# Arithmetic operations
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


