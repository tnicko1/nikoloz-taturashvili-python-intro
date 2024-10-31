def highest_common_factor(a, b):
    while b:
        a, b = b, a % b
    return a

def highest_common_factor_recursive(a, b):
    if b == 0:
        return a
    return highest_common_factor_recursive(b, a % b)

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a > 10000 or b > 10000 or a < 0 or b < 0:
        print("invalid input")
    else:
        print("GCD: ", highest_common_factor(a, b))
        print("GCD Recursive: ", highest_common_factor_recursive(a, b))