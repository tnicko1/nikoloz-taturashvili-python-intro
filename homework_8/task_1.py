print("Let's check if your string is palindrome")
string = input("Enter your string: ").lower().strip()
string = ''.join(e for e in string if e.isalnum())
if string == string[::-1]:
    print("Your string is palindrome")
else:
    print("Your string is not palindrome")