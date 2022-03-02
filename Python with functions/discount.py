# This program was type by Marcos Uc

# Libraries

from datetime import datetime 
import math

# variables

text = ""

#sales tax and discount %
sales_tax = 0.06
discount = 0.10

sub_total = 0

# While Loop
while text.lower() != "done":
    # Get the price from the user.
    print("When you finish type 'done' for continue")
    text = input("Please enter the price: ")
    if text.lower() != "done":
        price = float(text)

        quantity = int(input("Please enter the quantity: "))

        sub_total = price * quantity

sub_total = round(sub_total, 2)  


# Day of week
current_day = datetime.now()

day_of_week = current_day.weekday()

# operations
taxes = round(sub_total * sales_tax)
total = taxes + sub_total
total_discount = total * discount
amount_needed_for_disc = 50 - total

if day_of_week == 0 or day_of_week == 3 or day_of_week == 4 or day_of_week == 5 or day_of_week == 6:
    print(f"Sales tax amount: {taxes:.2f}")
    print(f"Total: {total:.2f}")
elif day_of_week == 1 or day_of_week == 2:
    if total >= 50:
        print(f"Discount amount: {total_discount:.2f}")
        total_with_discount = total - total_discount
        print(f"Sales tax amount: {taxes:.2f}")
        print(f"Your total with discount: {total_with_discount:.2f}")
    if total < 50:
        print(f"Sales tax amount: {taxes:.2f}")
        print(f"Total: {total:.2f}")
        print(f"You need {amount_needed_for_disc:.2f} for to get discount")
