"""
Write a function that takes an unspecified number of numeric arguments and returns the maximum.
Call the function multiple times for different arguments to demonstrate its performance.
"""

def find_maximum(*numbers):
    if not numbers:
        return None
    return max(numbers)

print(find_maximum(1, 2, 3))                # Output: 3
print(find_maximum(-1, -5, 0, 10))          # Output: 10
print(find_maximum(42))                              # Output: 42
print(find_maximum())                                # Output: None
print(find_maximum(1.5, 2.7, 0.9))          # Output: 2.7