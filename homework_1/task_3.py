import math

print("You are about to draw a triangle, please provide dimensions of all sides")
side_one = int(input("Enter side one: "))
side_two = int(input("Enter side two: "))
side_three = int(input("Enter side three: "))
perimeter = side_one + side_two + side_three
sub_perimeter = perimeter / 2
#Heron's formula
area = math.sqrt(sub_perimeter * (sub_perimeter - side_one) * (sub_perimeter - side_two) * (sub_perimeter - side_three))
print("The perimeter of the triangle is", perimeter)
print("The area of the triangle is", area)