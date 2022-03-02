# Pracitca de programa de venta de productos

# questions by variables
price_child_meal = float(input("What is the price of a child's meal? ")) 
price_adult_meal = float(input("What is the price of an adult's meal? ")) 
child_amount = int(input("How many children are there? "))
adult_amount = int(input("How many adults are there? "))
price_drink = float(input("What is the price of a drink? "))
drink_amount = int(input("How many drings? "))
price_chocolate_cake = float(input("what is the price of the chocolate cake? "))
chocolate_cake_amount = int(input("How many cakes? "))
tax = float(input("What is the sales tax rate? "))
print()
print("--------------------------------------------------")
#result for every question
subtotal = (price_child_meal * child_amount) + (price_adult_meal * adult_amount) + (price_drink * drink_amount) + (price_chocolate_cake * chocolate_cake_amount)
print(f"Subtotal ${subtotal:.2f}")
sales_tax = (subtotal * tax) / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
print()
pyment_amount = float(input("What is the pyment amount? $"))
change = pyment_amount - total
print(f"change: ${change:.2f}")
print("--------------------------------------------------")