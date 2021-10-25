# the code below will print a list of numbers btw 5 and 10 with an increment of 2
# -------------------------------------------------------------------------------
numbers = range(5, 10, 2)
for i in numbers:
    print(i)

print()
# code above simplified
# ---------------------
for i in range(5, 10, 2):
    print(i)

# -------------------------
print()
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# ------------------------
print()
for x in range(1, 5):
    print(x)

print()
# factorial
# --------------------------
a = 1
x = int(input("Enter a number: "))
for i in range(x, 1, -1):
    a = i * a
print(a)


print()
# factorial
# --------------------------
a = 1
x = int(input("Enter a number: "))
for i in range(1, x):
    a = i * a
print(a)
