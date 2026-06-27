import math

#Area of Circle
print("AREA OF CIRCLE")
radius = float(input("Enter radius of a circle: "))
area = math.pi * pow(radius, 2)

print(f"Area of a circle = {round(area, 2)} cm^2")

#Circumference of Circle
print("\nCIRCUMFERENCE OF CIRCLE")
circumference = 2 * math.pi * pow(radius, 2)

print(f"Circumference of a circle = {round(circumference, 2)} cm^2")

#Hypotenuse of a triangle
print("\nHYPOTENUSE OF TRIANGLE")
sideA = float(input("Enter side a: "))
sideB = float(input("Enter side b: "))

hyp = math.sqrt( pow(sideA, 2) + pow(sideB, 2))
print(f"Hypotenuse of triangle = {round(hyp, 2)} cm^2")