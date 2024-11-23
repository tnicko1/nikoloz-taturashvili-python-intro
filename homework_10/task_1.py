"""
Write a function that takes a text as an argument and counts the number of vowels in that text.
Call the function several times for different arguments to demonstrate its operation.
"""

def vowel_count(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1

    return count

# Test
print(vowel_count("hello"))  # 2
print(vowel_count("world"))  # 1
print(vowel_count("Python"))  # 1
print(vowel_count("Programming"))  # 3
print(vowel_count("Language"))  # 3