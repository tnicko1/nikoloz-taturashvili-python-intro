import task_2

def lowest_common_multiple(a, b):
    return a * b // task_2.highest_common_factor(a, b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("LCM: ", lowest_common_multiple(a, b))