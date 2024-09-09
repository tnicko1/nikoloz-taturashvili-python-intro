import math

print("You are about to draw a triangle, please provide dimensions of all sides")
sideOne = int(input("Enter side one: "))
sideTwo = int(input("Enter side two: "))
sideThree = int(input("Enter side three: "))
perimeter = sideOne + sideTwo + sideThree
subPerimeter = perimeter / 2
#Heron's formula
area = math.sqrt(subPerimeter * (subPerimeter - sideOne) * (subPerimeter - sideTwo) * (subPerimeter - sideThree))
print("The perimeter of the triangle is", perimeter)
print("The area of the triangle is", area)