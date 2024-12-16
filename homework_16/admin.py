from random import randint

from homework_16.common import process_user_input, animation
from homework_16.db import sessions


def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    print("5. sign out")
    return process_user_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")
    sign_in()

def sign_in():
    print("Enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    animation("Signing in", 1)
    if username == "admin" and password == "admin":
        print("Sign in successful")
    else:
        print("Sign in failed")
        return sign_in()

def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")
        print("\n")

def remove_session():
    print("Removing session")
    session_id = input("Enter session ID: ")
    animation("Removing session", 2)
    for session in sessions:
        if session_id == str(session["session_id"]):
            sessions.remove(session)
            print("Session removed successfully")
            return
    print("Session not found")

def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    session_id = len(sessions) + 1
    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")
    sessions.append(session)

def edit_session():
    print("Editing session")
    session_id = input("Enter session ID: ")
    animation("Editing session", 2)
    for session in sessions:
        if session_id == str(session["session_id"]):
            print("Enter the new session details")
            film_name = input("Film name: ")
            start_time = input("Start time: ")
            room_number = input("Room number: ")
            room_length = int(input("Room length: "))
            room_width = int(input("Room width: "))
            capacity = room_length * room_width
            session["film_name"] = film_name
            session["start_time"] = start_time
            session["room_number"] = room_number
            session["room_length"] = room_length
            session["room_width"] = room_width
            session["capacity"] = capacity
            print("Session edited successfully")
            return
    print("Session not found")

def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                remove_session()
            case "3":
                add_session()
            case "4":
                edit_session()
            case "5":
                animation("Signing out", 1)
                return
            case _:
                print("Invalid input")
