# lib/cli.py

import click
from helpers import add_room, list_rooms, book_room, update_room_price, delete_room

@click.group()
def cli():
    """Hotel Management CLI"""
    pass

@cli.command()
@click.option('--number', prompt='Room number', help='The room number')
@click.option('--type', prompt='Room type', help='The type of the room (e.g., single, double, suite)')
@click.option('--price', prompt='Room price', type=float, help='The price of the room')
def add(number, type, price):
    """Add a new room"""
    add_room(number, type, price)

@cli.command()
def list():
    """List all rooms"""
    list_rooms()

@cli.command()
@click.option('--number', prompt='Room number', help='The room number to book')
@click.option('--customer', prompt='Customer name', help='The name of the customer booking the room')
def book(number, customer):
    """Book a room"""
    book_room(number, customer)

@cli.command()
@click.option('--number', prompt='Room number', help='The room number to update')
@click.option('--price', prompt='New room price', type=float, help='The new price of the room')
def update(number, price):
    """Update the price of a room"""
    update_room_price(number, price)

@cli.command()
@click.option('--number', prompt='Room number', help='The room number to delete')
def delete(number):
    """Delete a room"""
    delete_room(number)

if __name__ == '__main__':
    cli()
