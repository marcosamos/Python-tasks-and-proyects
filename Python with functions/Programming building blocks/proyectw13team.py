import math

def square_area(side):
    return side * side

def rectangle_area(lenght, width):
    return lenght * width

def circle_area(radius):
    return math.pi * radius * radius

shape = ""

while shape != "quit":
    shape = input("what shape do you have? ")
    shape = shape.lower()

    if shape == "square":
        side = float(input("what is the lenght of the side "))
        area = square_area(side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        lenght = float(input("what is the lenght? "))
        width = float(input("what is the width? "))
        area = rectangle_area(lenght, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("what is the radius? "))
        area = circle_area(radius)
        print(f"The area is {area}")
