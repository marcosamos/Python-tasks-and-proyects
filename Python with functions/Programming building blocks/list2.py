# Practica de listas 2

print("Please enter the items of the shopping list (type: Quit to finish):")

shopping_list = []
item = None


while item != "Quit":
    item = input("Item: ")
    if item != "Quit":
        shopping_list.append(item)
print("The shopping list is: ")
for item in shopping_list:
    print(item)

print("The shopping list with indexes is:")
for item in range(len(shopping_list)):
    numbers = shopping_list[item]
    print(f"{item}. {numbers}")

index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

print("The shopping list with indexes is:")

for item in shopping_list:
    shopping_list.pop(index)
    shopping_list.append(new_item)
    print(item)
