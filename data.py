import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample JSON data
data = """
{
    "users": [
        {
            "id": 1,
            "name": "John Doe",
            "products": [
                {"id": 1, "name": "Laptop"},
                {"id": 2, "name": "Mouse"}
            ]
        }
    ]
}
"""

# Assuming the same setup as Approach 1

# Parse JSON
parsed_data = json.loads(data)

# Insert users and their products
for user_data in parsed_data['users']:
    user = User(id=user_data['id'], name=user_data['name'])
    session.add(user)
    for product in user_data['products']:
        product_instance = Product(id=product['id'], name=product['name'], user_id=user.id)
        session.add(product_instance)

session.commit()
