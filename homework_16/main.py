from homework_16.admin import admin_loop
from homework_16.common import process_user_input, animation
from homework_16.db import sessions

user_tickets = []

def list_menu_items():
    print("1. list sessions")
    print("2. search movie")
    print("3. buy ticket")
    print("4. my tickets")
    print("5. admin")
    return process_user_input()

def greetings():
    print("Welcome to the movie ticket booking system")
    print("Please enter EXIT to exit")

def list_sessions():
    print("Listing sessions")
    animation("Loading sessions", 2)
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"Film: {session['film_name']} | Room: {session['room_number']} | Session ID: {session['session_id']}")
    print("\n")

def search_movie():
    print("Searching movie")
    movie_name = input("Enter movie name: ")
    animation("Searching", 2)
    found = False
    for session in sessions:
        if movie_name.lower() in session["film_name"].lower():
            print(f"Film: {session['film_name']} | Room: {session['room_number']} | Session ID: {session['session_id']}\n")
            found = True
    if not found:
        print("No movie found\n")

def buy_ticket():
    print("Buying ticket")
    session_id = input("Enter session ID: ")
    animation("Buying ticket", 2)
    for session in sessions:
        if session_id == str(session["session_id"]):
            print(f"Ticket bought for {session['film_name']}")
            user_tickets.append(session)
            print("\n")
            return
    print("Session not found\n")

def list_tickets():
    print("Listing tickets")
    if not user_tickets:
        print("No tickets found")
        return
    for ticket in user_tickets:
        print(f"Film: {ticket['film_name']} | Room: {ticket['room_number']} | Session ID: {ticket['session_id']}")
    print("\n")

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                search_movie()
            case "3":
                buy_ticket()
            case "4":
                list_tickets()
            case "5":
                admin_loop()
                print("Admin panel closed")
            case _:
                print("Invalid input")

def main():
    greetings()
    program_loop()


if __name__ == "__main__":
    main()