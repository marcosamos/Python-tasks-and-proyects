# Programa para menu de una tienda de articulos
menu = None
menu_list = ["Add item","View cart", "Remove item", "Compute total", "Quit"]
item = None
item_list = []
item_cost = None
items_cost = []
total = 0

print("Welcome to the Shopping Cart Program!")
print()

while menu != 5:
    print("Please select one of the following:")
        
    for menu in range(len(menu_list)):
        index = menu_list[menu]
        print(f"{menu + 1}. {index}")

    user_option = int(input("Please enter an action: "))

    if user_option == 1:
        item = input("What item would you like to add? ")
        item_list.append(item)
        item_cost = float(input(f"What is the price of {item}? "))
        items_cost.append(item_cost)
        print(f"{item} has been added to the cart.")

    if user_option == 2:
        print("The contents of the shopping cart are:")
        for index in range(len(item_list)):
            item = item_list[index]
            print(f"{index + 1}. {item} - ${items_cost[index]:.2f}")

    if user_option == 3:
        remove = int(input("Which item would you like to remove? ")) - 1
        for index in range(len(item_list)):
            if remove != index:
                print("Sorry, that is not a valid item number.")
            else:
                item_list.pop(remove)
                items_cost.pop(remove)
                print("Item removed")

    if user_option == 4:
        for cost in items_cost:
            total += cost
        print(f"The total price of the items in the shopping cart is ${total}")

    if user_option == 5:
        menu = 5
print("Thank you. Goodbye.")