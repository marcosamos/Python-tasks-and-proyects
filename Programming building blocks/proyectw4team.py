import math
print("Welcome to the velocity calculator. Please enter the following:")
print()
m = float(input("mass (in Kg): "))
g = float(input("Grabity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in Kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
c = (1 / 2) * p * A * C
v_at_t = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
print()
print(f"The inner value of c is: {c:.3f} m/s")
print(f"The velocity after {t} seconds is: {v_at_t:.3f} m/s")