import math
pi = math.pi
radius = float(input("Enter radius: "))
area = round(pi * (radius**2),3)
circum = round(2*pi*radius,3)


print("Area =", area)
print("Circumference =",circum)
