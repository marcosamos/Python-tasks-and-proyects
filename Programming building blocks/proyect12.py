#Marcos Uc
#Questions
interest_year = int(input("Enter the year of interest: "))

#other_variables
total = 0

#lower variables1
lower_value_life_expectancy = -1
lower_country = ""
year_lower = 0

#highest variables1
highest_value_life_expectancy = 100000
highest_country = ""
year_highest = 0

#lower variables2
lower_value_life_expectancy2 = -1
lower_country2 = ""

#highest variables2
highest_value_life_expectancy2 = 100000
highest_country2 = ""

#program
with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    for line in life_expectancy:
        parts = line.split(",")

        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy_year = float(parts[3])

        if life_expectancy_year > lower_value_life_expectancy:
            lower_value_life_expectancy = life_expectancy_year
            lower_country = entity
            year_lower = year
        if life_expectancy_year < highest_value_life_expectancy:
            highest_value_life_expectancy = life_expectancy_year
            highest_country = entity
            year_highest = year
        
        if year == interest_year:

            total = total =+ life_expectancy_year
                 

            if life_expectancy_year > lower_value_life_expectancy2:
                lower_value_life_expectancy2 = life_expectancy_year
                lower_country2 = entity

            if life_expectancy_year < highest_value_life_expectancy2:
                highest_value_life_expectancy2 = life_expectancy_year
                highest_country2 = entity
        

print("o-------------*--------------------------------*----------------o")
print()
print(f"The overall max life expectancy is: {lower_value_life_expectancy} from {lower_country} in {year_lower}")
print(f"The overall min life expectancy is: {highest_value_life_expectancy} from {highest_country} in {year_highest}")
print()
print(f"For the year {interest_year}:")
print()
print(f"The average life expectancy across all countries was {total}")
print()
print(f"The max life expectancy was in {lower_value_life_expectancy2} with {lower_country2} in {interest_year}")
print()
print(f"The min life expectancy was {highest_value_life_expectancy2} with {highest_country2} in {interest_year}")
print("o-------------*--------------------------------*----------------o")