import numpy as np

class CinemaApp:
    def __init__(self):
        self.sessions = {}
        self.ticket_prices = {}
        self.secret_admin_password = "adminpass"

    def display_seating(self, session_name):
        """Visualize cinema seats for a session using numpy."""
        if session_name not in self.sessions:
            print("Session not found.")
            return

        seats = self.sessions[session_name]
        print("Cinema Room Layout:")
        for row in seats:
            print(" ".join("\033[94m●\033[0m" if seat == 0 else "\033[91m●\033[0m" for seat in row))
        print("\033[94m●\033[0m = Available, \033[91m●\033[0m = Taken\n")

    def list_sessions(self):
        if not self.sessions:
            print("No ongoing sessions.")
            return

        print("Ongoing Sessions:")
        for name, seats in self.sessions.items():
            available_seats = np.sum(seats == 0)
            print(f" - {name}: {available_seats} available seats (${self.ticket_prices[name]} per ticket)")
        print()

    def search_movie(self, movie_name):
        if movie_name in self.sessions:
            print(f"{movie_name} is available!")
            self.display_seating(movie_name)
        else:
            print(f"{movie_name} is not available.\n")

    def buy_ticket(self, movie_name):
        if movie_name not in self.sessions:
            print("Session not found.")
            return

        print(f"Buying a ticket for {movie_name}.")
        self.display_seating(movie_name)

        try:
            row = int(input("Enter the row number: "))
            col = int(input("Enter the column number: "))

            if self.sessions[movie_name][row, col] == 0:
                self.sessions[movie_name][row, col] = 1
                print("Ticket purchased successfully!")
            else:
                print("Seat already taken.")
        except (ValueError, IndexError):
            print("Invalid seat selection.")

    def add_session(self):
        movie_name = input("Enter movie name: ")
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of seats per row: "))
        price = float(input("Enter ticket price: "))

        self.sessions[movie_name] = np.zeros((rows, cols), dtype=int)
        self.ticket_prices[movie_name] = price
        print(f"Session '{movie_name}' added.\n")

    def edit_session(self):
        movie_name = input("Enter the name of the session to edit: ")
        if movie_name not in self.sessions:
            print("Session not found.")
            return

        rows = int(input("Enter new number of rows: "))
        cols = int(input("Enter new number of seats per row: "))
        price = float(input("Enter new ticket price: "))

        self.sessions[movie_name] = np.zeros((rows, cols), dtype=int)
        self.ticket_prices[movie_name] = price
        print(f"Session '{movie_name}' updated.\n")

    def remove_session(self):
        movie_name = input("Enter the name of the session to remove: ")
        if movie_name in self.sessions:
            del self.sessions[movie_name]
            del self.ticket_prices[movie_name]
            print(f"Session '{movie_name}' removed.\n")
        else:
            print("Session not found.")

    def change_ticket_price(self):
        movie_name = input("Enter the name of the session: ")
        if movie_name in self.ticket_prices:
            price = float(input("Enter the new ticket price: "))
            self.ticket_prices[movie_name] = price
            print(f"Ticket price for '{movie_name}' updated to ${price:.2f}.\n")
        else:
            print("Session not found.")

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. List sessions")
            print("2. Search for a movie")
            print("3. Buy a ticket")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.list_sessions()
            elif choice == "2":
                movie_name = input("Enter movie name: ")
                self.search_movie(movie_name)
            elif choice == "3":
                movie_name = input("Enter movie name: ")
                self.buy_ticket(movie_name)
            elif choice == "4":
                print("Exiting user menu.")
                break
            else:
                print("Invalid choice.")

    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add a session")
            print("2. Edit a session")
            print("3. Remove a session")
            print("4. Change ticket price")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_session()
            elif choice == "2":
                self.edit_session()
            elif choice == "3":
                self.remove_session()
            elif choice == "4":
                self.change_ticket_price()
            elif choice == "5":
                print("Exiting admin menu.")
                break
            else:
                print("Invalid choice.")

    def run(self):
        while True:
            print("\n--- Cinema Management ---")
            print("1. User")
            print("2. Admin")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.user_menu()
            elif choice == "2":
                password = input("Enter admin password: ")  # Use input() instead of getpass.getpass()
                if password == self.secret_admin_password:
                    print("Admin access granted.")
                    self.admin_menu()
                else:
                    print("Incorrect password.")
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = CinemaApp()
    app.run()