print("Enter a list of number, type 0 when finished")
number = -1
numbers = []
#First step
while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

#second step
count = len(numbers)
average = sum / count

print(f"The average is: {average}")

#Third step, I found 2 ways for show the max.
max_value = max(numbers)

print("The largest number is:", max_value)

#max = -1

#for number in numbers:
#    if number > max:
#        max = number
#print(f"The largest number is: {max}")




