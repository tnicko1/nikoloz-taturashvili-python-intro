from random import randint


def draw_sign():
    random_number = randint(1, 3)
    if random_number == 1:
        sign = "Rock"
    elif random_number == 2:
        sign = "Paper"
    else:
        sign = "Scissors"
    return sign


def print_winner(user_choice, computer_choice, winner: bool):
    if user_choice == 1:
        user_choice_str = "Rock"
    elif user_choice == 2:
        user_choice_str = "Paper"
    else:
        user_choice_str = "Scissors"

    winner_text = f"\nYou chose {user_choice_str}\nComputer chose {computer_choice}\nYou Won!" if winner == True else f"\nYou chose {user_choice_str}\nComputer chose {computer_choice}\nComputer Won!"
    print(winner_text)


def determine_winner(user_choice, computer_choice):
    if user_choice == 1 and computer_choice == "Scissors":
        print_winner(user_choice, computer_choice, True)
    elif user_choice == 2 and computer_choice == "Rock":
        print_winner(user_choice, computer_choice, True)
    elif user_choice == 3 and computer_choice == "Paper":
        print_winner(user_choice, computer_choice, True)
    elif user_choice == 1 and computer_choice == "Paper":
        print_winner(user_choice, computer_choice, False)
    elif user_choice == 2 and computer_choice == "Scissors":
        print_winner(user_choice, computer_choice, False)
    elif user_choice == 3 and computer_choice == "Rock":
        print_winner(user_choice, computer_choice, False)
    else:
        return True


def main():
    while True:
        try:
            user_choice = int(input("Choose a sign\n1. Rock\n2. Paper\n3. Scissors\nYour choice: "))
            if user_choice < 1 or user_choice > 3:
                print("\nInvalid input. Number must be between 1 and 3\n")
                continue

            computer_choice = draw_sign()
            is_tie = determine_winner(user_choice, computer_choice)
            if is_tie:
                print("\nIt's a tie!, Try again!\n")
                continue
        except ValueError:
            print("\nInvalid input. Please input a number\n")
            continue
        break


if __name__ == '__main__':
    main()