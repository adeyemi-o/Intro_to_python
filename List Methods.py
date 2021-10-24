# List Method
# ----------------------------------
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # add a new number to the list
print(numbers)

# insert method
# ----------------------------------
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)  # insert item
print(numbers)

# remove & clear method
# ----------------------------------
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  # remove item
print(numbers)
numbers.clear()  # removes all values in the list
print(numbers)

# in operator
# ----------------------------------
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # check if a value exists in the list, it will return a boolean value

# len function (note: its a built in function like print)
# ----------------------------------
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # returns number of elements in a list
