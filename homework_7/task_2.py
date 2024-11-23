"""
The program should let us input a word and print only the consonants from that word.
"""

user_input = input("Enter a string: ")
for i in range(len(user_input)):
    if user_input[i] in "aeiouAEIOU":
        continue
    print(user_input[i], end="")