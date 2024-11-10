def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(5))  # True
print(is_prime(6))  # False
print(is_prime(11))  # True
print(is_prime(12))  # False
print(is_prime(13))  # True
print(is_prime(14))  # False