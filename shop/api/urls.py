from django.urls import path
from .views import (
    UserList,
    UserDetail,
    ProductList,
    ProductDetail,
    OrderList,
    OrderDetail,
)

# URL patterns for the shop API.
# Each endpoint maps to a corresponding view for users, products, and orders.

urlpatterns = [
    # User endpoints
    path('users/', UserList.as_view()),              # List all users or create a new user
    path('users/<str:pk>/', UserDetail.as_view()),   # Retrieve, update, or delete a specific user by primary key

    # Product endpoints
    path('products/', ProductList.as_view()),        # List all products or create a new product
    path('products/<str:pk>/', ProductDetail.as_view()), # Retrieve, update, or delete a specific product by primary key

    # Order endpoints
    path('orders/', OrderList.as_view()),            # List all orders or create a new order
    path('orders/<str:pk>/', OrderDetail.as_view()), # Retrieve, update, or delete a specific order by primary key
]
