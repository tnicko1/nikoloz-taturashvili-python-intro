"""
Write a program that will take a string and determine whether it is a palindrome.
A palindrome is a word that reads the same from left to right.
For example: radar, level, racecar are palindromes.
The program should also identify a palindrome sentence.
It should ignore all characters except the English characters a-z, A-Z.
The program should ignore the case of the character, Racecar is a palindrome.
"""

print("Let's check if your string is palindrome")
string = input("Enter your string: ").lower().strip()
string = ''.join(e for e in string if e.isalnum())
if string == string[::-1]:
    print("Your string is palindrome")
else:
    print("Your string is not palindrome")