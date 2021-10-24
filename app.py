# Introduction to python - Mosh Youtube Classes
# ---------------------------------------------
# print('patient Check in Data')
# print('---------------------')
# patient = 'James Smith'
# age = '35'
# date = '10-10-2021'
#
# print('Patient      Age     Date')
# print(patient,     age, date)

# ------------------------------------
# input function
# ------------------------------------
name = input('What is your name? ')
# concatenation of values using (+)
print('Hello ' + name)

birth_year = input('Enter your birth year: ')
# convert string birth_year to int
age = 2020 - int(birth_year)
# convert age from int to str, concatenate with other values and print out
print(name + ', you are ' + str(age) + ' years old')
print('')
# simple calculator program
# ---------------------------
print('Simple Calculator Program')
print('-------------------------')
first_num = input('First Number: ')  # or first_num = float(input('First Number: '))
second_num = input('Second Number: ')  # or second_num = float(input('Second Number: '))
sum = float(first_num) + float(second_num)  # - sum = first_num + second_num
print('Answer is: ' + str(sum))


