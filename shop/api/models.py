# Import necessary modules from mongoengine and datetime
from mongoengine import (
    Document, StringField, FloatField, ReferenceField, ListField, DateTimeField
)
from datetime import datetime

# User model: Represents a user in the system
class User(Document):
    username = StringField(required=True, unique=True)  # Unique username for each user
    email = StringField(required=True)                  # User's email address
    password = StringField(required=True)               # User's password (should be hashed in production)

# Product model: Represents a product available for purchase
class Product(Document):
    name = StringField(required=True)                   # Name of the product
    description = StringField()                         # Optional description of the product
    price = FloatField(required=True)                   # Price of the product

# Order model: Represents an order placed by a user
class Order(Document):
    user = ReferenceField(User, required=True)          # Reference to the user who placed the order
    products = ListField(ReferenceField(Product))       # List of products in the order
    created_at = DateTimeField(default=datetime.utcnow) # Timestamp when the order was created

"""
Code Explanation:
- The code defines three MongoDB document models using mongoengine: User, Product, and Order.
- User stores user credentials (username, email, password).
- Product stores product details (name, description, price).
- Order links a user to a list of products and records the order creation time.
- ReferenceField is used to create relationships between documents (Order to User/Product).
"""
