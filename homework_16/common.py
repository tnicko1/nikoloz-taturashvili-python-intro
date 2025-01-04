from time import sleep, time

def animation(string_to_animate, duration = 5):
    end_time = time() + duration
    while time() < end_time:
        for i in range(4):  # Cycle through 0, 1, 2, 3 dots
            dots = "." * i
            print(f"\r{string_to_animate}{dots}",end="")  # \r resets the line
            sleep(0.5)
    print("\r", end="")  # Clear the line

def process_user_input():
    user_input = input("->: ").lower()
    if user_input not in ["1", "2", "3", "4","5", "exit"]:
        print("Invalid input")
        return process_user_input()
    if user_input == "exit":
        print("Goodbye")
        exit()
    return user_input
