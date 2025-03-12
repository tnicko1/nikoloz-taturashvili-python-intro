# Cinema Management Application

## Overview

This is a Python-based Cinema Management Application that allows users to interact with a cinema ticket booking system. The application provides both user and admin functionalities for managing movie sessions, viewing seating arrangements, and purchasing tickets.

## Features

### User Functions
- List available movie sessions
- Search for specific movies
- View seating arrangements
- Purchase tickets

### Admin Functions
- Add new movie sessions
- Edit existing sessions
- Remove sessions
- Change ticket prices

## Requirements

- Python 3.x
- NumPy library

## Installation

1. Clone the repository
2. Ensure you have NumPy installed:
   ```
   pip install numpy
   ```

## How to Run

Run the script directly:
```bash
python cinema_app.py
```

## Usage Guide

### Main Menu
- **User**: Browse and purchase tickets
- **Admin**: Manage cinema sessions (password required)

### User Menu Options
1. List sessions
2. Search for a movie
3. Buy a ticket
4. Exit

### Admin Menu Options
1. Add a session
2. Edit a session
3. Remove a session
4. Change ticket price
5. Exit

## Admin Access

- Default admin password: `adminpass`
- **Note**: Change this password in the source code for security

## Seating Visualization

The application uses color-coded visualization:
- 🔵 Blue (●): Available seats
- 🔴 Red (●): Taken seats

## Technology Stack

- Language: Python
- Libraries: NumPy
- Features: Object-Oriented Programming, Session Management, Interactive CLI

## Potential Improvements
- Add persistent storage (database/file)
- Implement more robust password management
- Add more detailed error handling
- Create user authentication system
- Implement seat reservation timeout