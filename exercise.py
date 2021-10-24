# ----------------------------------
# A program to print out weight in Kg or Lbs
# ----------------------------------
weight = int(input("What is your weight: "))
unit = input("(k)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight * 2.2
    print("Your weight in Lbs is: " + str(converted) + "Lbs")
else:
    converted = weight / 2.2
    print("Your weight in kgs is: " + str(converted) + "Kgs")
