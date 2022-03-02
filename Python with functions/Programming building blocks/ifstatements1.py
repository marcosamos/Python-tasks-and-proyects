#Uso de condicionales

#asks the user for two integers

integer_1 = int(input("Plese, insert a integer: "))
integer_2 = int(input("Plese, insert a integer: "))
if integer_1 > integer_2:
    print("The first number is greater")
else:
    print("The first number is not greater")

if integer_1 == integer_2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if integer_2 > integer_1:
    print("The second number is greater")
else:
    print("The second number is not greater")
print()
user_animal = input("What is your favorite animal? ")
if user_animal.lower() == "turtle":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")