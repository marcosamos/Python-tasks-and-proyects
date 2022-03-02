import math
user_number = int(input("How many columns and rows do you want in your multiplication table? "))
max_number = user_number * user_number
digits = int(math.log10(max_number)) + 1
range_size = user_number + 1

for row_number in range(1, range_size):
    for col_number in range(1, range_size):
        number = row_number * col_number
        print(f"{number:{digits}}", end=" ")
    print()