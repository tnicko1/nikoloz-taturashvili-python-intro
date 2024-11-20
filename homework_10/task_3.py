def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return "Invalid input"
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(6))  # Output: 720
print(factorial(4))  # Output: 24
print(factorial(-2))  # Output: "Invalid input"