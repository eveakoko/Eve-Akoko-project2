# lib/setup_db.py
from models.hotel import Base, engine

def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created.")

if __name__ == '__main__':
    create_tables()
