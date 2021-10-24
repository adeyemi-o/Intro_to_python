# Tuples are like list but immutable, hence cannot be changed.
#  ----------------------------------------------------------
numbers = (1, 2, 3, 7, 8)  # square brackets[] are used for lists while parenthesis for Tuples
# numbers[0] = 3  # TypeError: 'tuple' object does not support item assignment
x = numbers.index(8)
print(x)
