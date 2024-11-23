"""
(*) Write a program that encrypts or decrypts the text entered by the user and prints it on the screen.
Leave any characters that are not a-z unchanged.
The encryption logic is as follows, each character (a-z) should be replaced by the character to its right on the keyboard.
If there is no English character to the right of the character on the keyboard,
then it should go to the first character from this string.
For example: p -> q, l -> a. etc.

The program should convert only lowercase English characters a-z.
Example 1:
Enter action (e/d): e
Enter text: power
qpert

Example 2:
Enter action (e/d): d
Enter text: quyjpm
python
"""

qwerty = "qwertyuiopasdfghjklzxcvbnm"

choice = input("Encrypt or Decrypt (e/d): ").lower()
if choice != 'e' and choice != 'd':
    print("Invalid choice")
elif choice == 'e':
    user_input = input("Enter a string: ").lower()
    for i in range(len(user_input)):
        if user_input[i] == 'p':
            user_input = user_input.replace('p', 'q')
        elif user_input[i] == 'l':
            user_input = user_input.replace('l', 'a')
        elif user_input[i] == 'm':
            user_input = user_input.replace('m', 'z')
        else:
            user_input = user_input.replace(user_input[i], qwerty[qwerty.index(user_input[i]) + 1])

    print(user_input)
else:
    user_input = input("Enter a string: ")
    for i in range(len(user_input)):
        if user_input[i] == 'q':
            user_input = user_input.replace('q', 'p')
        elif user_input[i] == 'a':
            user_input = user_input.replace('a', 'l')
        elif user_input[i] == 'z':
            user_input = user_input.replace('z', 'm')
        else:
            user_input = user_input.replace(user_input[i], qwerty[qwerty.index(user_input[i]) - 1])
    print(user_input)