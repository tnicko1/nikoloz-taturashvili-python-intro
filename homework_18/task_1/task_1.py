"""
Write a program that reads the data.txt file.
The data.txt file contains product purchase data.
The data is separated by a comma.
The data sequence is as follows: user_name,product_name,amount,price - where price is the unit price of the product.
The program should create two new files, small.txt and high.txt.
The program should write to the small.txt file all purchases whose value is less than 10,
and to the high.txt file all the others.
"""

file = open("data.txt", "r")
file_data = file.read()
file.close()

small = open("small.txt", "w")
high = open("high.txt", "w")

for line in file_data.split('\n')[1:]:
    properties = line.split(',')
    if float(properties[3]) < 10:
        small.write(f"{properties[1]},{properties[3]}\n")
    else:
        high.write(f"{properties[1]},{properties[3]}\n")

small.close()
high.close()

print(file_data)