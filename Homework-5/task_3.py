num = int(input("Enter a number (max: 20): "))

if num > 20 or num < 0:
    print("Please enter a number between 0 and 20")
else:
    a, b = 0, 1
    count = 0
    while count <= num:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
        """
        Task said not to use lists, this behind the scenes is using lists so if it counts as using one,
        alternative would be to create a 'temp' variable and swap the values of a and b using that.
        """