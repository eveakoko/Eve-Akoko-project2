from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DATABASE_URL = "sqlite:///hotel.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    is_booked = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Room(number={self.number}, type={self.type}, price={self.price}, is_booked={self.is_booked})>"
