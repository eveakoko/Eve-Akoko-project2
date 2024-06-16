from models.hotel import Room, session

def add_room(number, type, price):
    room = Room(number=number, type=type, price=price)
    session.add(room)
    session.commit()
    print(f"Added: {room}")

def list_rooms():
    rooms = session.query(Room).all()
    for room in rooms:
        print(room)

def book_room(number, customer_name):
    room = session.query(Room).filter_by(number=number).first()
    if room:
        if not room.is_booked:
            room.is_booked = True
            session.commit()
            print(f"Room {number} booked successfully for {customer_name}.")
        else:
            print(f"Room {number} is already booked.")
    else:
        print(f"Room {number} not found.")

def update_room_price(number, new_price):
    room = session.query(Room).filter_by(number=number).first()
    if room:
        room.price = new_price
        session.commit()
        print(f"Updated Room {number} price to ${new_price}.")
    else:
        print(f"Room {number} not found.")

def delete_room(number):
    room = session.query(Room).filter_by(number=number).first()
    if room:
        session.delete(room)
        session.commit()
        print(f"Deleted Room {number}.")
    else:
        print(f"Room {number} not found.")
