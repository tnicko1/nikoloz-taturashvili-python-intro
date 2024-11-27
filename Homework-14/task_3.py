def fibonacci(n):
    if n <= 0:
        return tuple()

    if n == 1:
        return (0,)

    a, b = 0, 1
    result = [a, b]

    while len(result) < n:
        result.append(a + b)
        a, b = b, a + b

    return tuple(result)


print("First 5 numbers:", fibonacci(5))
print("First 8 numbers:", fibonacci(8))
print("Empty case:", fibonacci(0))
print("Single number:", fibonacci(1))
