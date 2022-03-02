# This program was wrote by Marcos Uc

# Libraries
import math



# Functions

def main():
    #list (Name, radius, height, cost)
    can_list = [
    ["#1 Picnic",	6.83,	10.16,	0.28],
    ["#1 Tall",	7.78,	11.91,	0.43],
    ["#2", 8.73, 11.59, 0.45],
    ["#2.5",	10.32,	11.91,	0.61],
    ["#3 Cylinder",	10.79,	17.78,	0.86],
    ["#5",	13.02,	14.29,	0.83],
    ["#6Z",	5.40,	8.89,	0.22],
    ["#8Z short",	6.83,	7.62,	0.26],
    ["#10",	15.72,	17.78,	1.53],
    ["#211",	6.83,	12.38,	0.34],
    ["#300",	7.62,	11.27,	0.38],
    ["#303",	8.10,	11.11,	0.42]
    ]
    # variables for IF statements
    good_efficiency = None
    max_efficiency = -1
    good_cost = None
    max_cost_efficiency = -1
         
    for name, radius, height, cost in can_list:

        can_efficiency = storage_efficiency(radius,height)
        cost_per_can = cost_efficiency(radius,height,cost)
        print(f"Name: {name}, Efficiency: {can_efficiency:.1f}, Cost: {cost_per_can:.2f}")

        # if statements
        if can_efficiency > max_efficiency:
            good_efficiency = name
            max_efficiency = can_efficiency

        if cost_per_can > max_cost_efficiency:
            good_cost = name
            max_cost_efficiency = cost_per_can

    print(f"Best can size in storage efficiency:, {good_efficiency}")
    print(f"Best can size in cost efficiency:, {good_cost}")


def storage_efficiency(radius, height):
    volume = cylider_volume(radius,height)
    surface_area = cylinder_surface_area(radius,height)
    can_efficiency = volume / surface_area
    return can_efficiency

def cost_efficiency(radius, height,cost):
    volume = cylider_volume(radius,height)
    cost_per_can = volume / cost
    return cost_per_can


def cylider_volume(radius, height):
    volume = math.pi * radius**2 * height

    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area



main()