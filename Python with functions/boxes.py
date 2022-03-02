import math


def boxes():
    items_box = int(input("Enter the number of items: "))
    items_per_box = int(input("Enter the number of items per box: "))
    boxes = math.ceil(items_box / items_per_box)
    print(f"For {items_box} items, packing {items_per_box} items in each box, you will need {boxes} boxes.")


boxes()