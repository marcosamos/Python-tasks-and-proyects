import math
temperature = 0
def wind_chill_calculation(temperature, wind):
    return  35.74 + (.6215 * temperature) - (35.75 * wind ** 0.16) + 0.4275 * temperature * (wind **0.16)

def celsius_conversion(temperature):
    temperature = (temperature_choice * (9/5)) + 32
    return temperature

temperature_choice = float(input("What is the temperature? "))
choice_degrees = input("Farenheit or Celsius (F or C)? ")

for wind in range(5, 61, 5):
   if choice_degrees.lower() == "C":
        temperature_choice = celsius_conversion(temperature)
        wind_chill_calculation = (celsius_conversion, wind)
        print(f"At temperature {temperature}, and wind speed {wind} mph, the windchill is: {wind_chill_calculation(celsius_conversion, wind):.2f}F")
   elif choice_degrees.lower() == "C":
        temperature_choice = temperature
        wind_chill_calculation = (temperature, wind)
        print(f"At temperature {temperature}, and wind speed {wind} mph,  the windchill is: {wind_chill_calculation(temperature, wind):.2f}F")