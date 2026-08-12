import math
#User must enter the first coordinate of a point that belongs in x axis and followed by the rest
#Must follow the distance formula where d = sqr(x^2 - x^1)^2 + (y^2 - y^1)^2

x1 = float(input("Enter x coordinate of the first point: "))
x2 = float(input("Enter x coordinate of the second point: "))
y1 = float(input("Enter y coordinate of the first point: "))
y2 = float(input("Enter y coordinate of the second point: "))

#Distance formula converted into code
distance = math.sqrt(x2 - x1)**2 + (y2 - y1)**2

#User  input result or the result of the coordinated points.
print()
print("--- Result ---")
print(f"The distance of the 2 points is: {distance:.2f}")