# This file was created by Marcos Uc
# Copyright.

# Libraries
import math
from datetime import datetime

# Variables
w = float(input("Enter the width of the tire in mm "))
a = float(input("Enter the spect ratio of the tire "))
d = float(input("Enter the diameter of the wheel in inches "))
t_number = 0

# Diferents tire and prices.
# Try with this dimentions. 
tire_1 = w == 195 and a == 65 and d == 15
tire_2 = w == 155 and a == 70 and d == 13
tire_3 = w == 185 and a == 65 and d == 14
tire_4 = w == 165 and a == 60 and d == 14

# Ecuation
volume = ((math.pi * (w**2)) * a) * (w * a + 2540 * d) / 10000000000
print("--------------------+--------------------")
# Ecuation Result
print(f"The approximate volume is {volume:.2f} liters")
print("--------------------+--------------------")



if w or a or d == tire_1 or tire_2 or tire_3 or tire_4:
    if tire_1:
        print("The price is 1169 MXN")
        purchase_chosse = input("Do you want to buy? yes or no   ")
        if purchase_chosse == "yes":
            t_number = int(input("Please type your Telephone Number: "))  
        else:
            print("Thank you for consult")
    elif tire_2:
        print("The price is 3154.44 MXN")
        purchase_chosse = input("Do you want to buy? yes or no   ")
        if purchase_chosse == "yes":
            t_number = int(input("Please type your Telephone Number: "))
        else:
            print("Thank you for consult")
    elif tire_3:
        print("The price is 4407.84 MXN")
        purchase_chosse = input("Do you want to buy? yes or no   ")
        if purchase_chosse == "yes":
            t_number = int(input("Please type your Telephone Number: "))
        else:
            print("Thank you for consult")
    elif tire_4:
        print("The price is 4407.84 MXN")
        purchase_chosse = input("Do you want to buy? yes or no   ")
        if purchase_chosse == "yes":
            t_number = int(input("Please type your Telephone Number: "))
        else:
            print("Thank you for consult")
else:
    print("Thank you for consult")
    current_day = datetime.now()
    print(current_day)
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_day}, {w}, {a}, {d}, {volume:.2f}", file=volumes_file)
print("--------------------+--------------------")
 # Current day and current hour
current_day = datetime.now()
print(current_day)
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_day}, {w}, {a}, {d}, {volume:.2f} Telephone number: {t_number}", file=volumes_file)