"""
Write a program that accepts two strings.
The program should check whether it is possible to obtain a second string using the characters of one string.
"""

def easter_egg():
    print("I am lord Voldemort!")
    exit(1)

print("Input two strings to check if they are anagrams")
string1 = input("Enter your first string: ").lower().strip()
string1 = ''.join(e for e in string1 if e.isalnum())

if string1 == "tommarvoloriddle": # easter egg for harry potter fans :)
    easter_egg()

string2 = input("Enter your second string: ").lower().strip()
string2 = ''.join(e for e in string2 if e.isalnum())

if sorted(string1) == sorted(string2):
    print("Your strings are anagrams")
else:
    print("Your strings are not anagrams")

