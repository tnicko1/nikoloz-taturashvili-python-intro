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