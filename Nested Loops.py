a = ["Janet", "George", "John", "Helen", "Robert", "Juliet"]
print(len(a))  # print the length of a

for i in range((len(a)-1), -1, -1):
    print(i, a[i])

print()
for i in range(1, 5):
    for j in range(1, 4):
        print(i * j, '\t')  # \t - tab
    print("\n")  # \n - new line

# ---------------------------------------
print()
x = int(input("Enter a number: "))
for i in range(x):
    for j in range(i+1):
        print("*")
    print("\n")
