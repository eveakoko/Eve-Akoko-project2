# Eve-Akoko-project2# Akoko-project 

This project is a simple Command Line Interface (CLI) application for managing a hotel using SQLAlchemy ORM and Click. It allows users to perform CRUD operations on rooms, such as adding rooms, listing available rooms, booking rooms, updating room prices, and deleting rooms.

## Files

- `lib/cli.py`: The main entry point of the application. It provides the user interface using Click.
- `lib/helpers.py`: Contains helper functions for managing hotel operations such as adding rooms, listing rooms, booking rooms, updating room prices, and deleting rooms.
- `lib/models/hotel.py`: Defines the data models for the hotel management system using SQLAlchemy ORM, including the `Room` model.

## How to Run

1. Install dependencies with `pipenv install`.
2. Start a pipenv shell with `pipenv shell`.
3. Run the CLI with `python lib/cli.py` followed by the desired command.

## Commands

- `python lib/cli.py add`: Adds a new room.
- `python lib/cli.py list`: Lists all rooms.
- `python lib/cli.py book`: Books a room.
- `python lib/cli.py update`: Updates the price of a room.
- `python lib/cli.py delete`: Deletes a room.

## Models

- `Room`: Represents a room with a number, type, price, and booking status.
