"""
Write a program that is given the number n.
The program should generate a sequence for the number n.
The first element of the sequence is n. Each subsequent element is determined by the following rule.
If the previous member is even - divide the previous member by 2 if the previous member is odd - multiply the previous member by 3 and add 1.
The sequence generation should stop when the number 1 is reached.

To generate the sequence, make 2 functions, one ordinary, the other with caching.
Make the caching a little different from the one discussed in the lecture.
In the caching discussed in the section, we had one value for one key, here we store many values for one key.
For example, if you cache n=3, the values should be 10, 5, 16, 8, 4, 2, 1.
"""

def generate_sequence(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def generate_sequence_with_cashing(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    sequence = [n]
    if n != 1:
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.extend(generate_sequence_with_cashing(next_n, cache))

    cache[n] = sequence
    return sequence

print(generate_sequence(5))

print(generate_sequence_with_cashing(7)) # calculates the sequence
print(generate_sequence_with_cashing(7)) # returns the cached sequence
print(generate_sequence_with_cashing(14)) # calculates up to 7 and then uses the cached sequence
