from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Product, Order
from .serializers import UserSerializer, ProductSerializer, OrderSerializer

# ----------------------------------------------------
# User CRUD API Views
# ----------------------------------------------------

class UserList(APIView):
    """
    API view to list all users or create a new user.

    GET: Returns a list of all users.
    POST: Creates a new user with provided data.
    """
    def get(self, request):
        # Retrieve all users from the database
        users = User.objects.all()
        # Serialize user data
        serializer = UserSerializer(users, many=True)
        # Return serialized data as response
        return Response(serializer.data)

    def post(self, request):
        # Deserialize and validate incoming user data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Save new user to the database
            user = serializer.save()
            # Return the created user data
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    API view to retrieve, update, or delete a user instance.

    GET: Returns details of a specific user.
    PUT: Updates a specific user.
    DELETE: Deletes a specific user.
    """
    def get_object(self, pk):
        # Helper method to get user by primary key
        return User.objects(id=pk).first()

    def get(self, request, pk):
        # Retrieve user instance
        user = self.get_object(pk)
        if not user:
            # Return 404 if user not found
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Serialize and return user data
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        # Retrieve user instance
        user = self.get_object(pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Deserialize and validate incoming data
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            # Save updated user
            user = serializer.save()
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Retrieve user instance
        user = self.get_object(pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# Product CRUD API Views
# ----------------------------------------------------

class ProductList(APIView):
    """
    API view to list all products or create a new product.

    GET: Returns a list of all products.
    POST: Creates a new product with provided data.
    """
    def get(self, request):
        # Retrieve all products from the database
        products = Product.objects.all()
        # Serialize product data
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize and validate incoming product data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # Save new product to the database
            product = serializer.save()
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    """
    API view to retrieve, update, or delete a product instance.

    GET: Returns details of a specific product.
    PUT: Updates a specific product.
    DELETE: Deletes a specific product.
    """
    def get_object(self, pk):
        # Helper method to get product by primary key
        return Product.objects(id=pk).first()

    def get(self, request, pk):
        # Retrieve product instance
        product = self.get_object(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        # Retrieve product instance
        product = self.get_object(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Deserialize and validate incoming data
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            # Save updated product
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Retrieve product instance
        product = self.get_object(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete product
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# Order CRUD API Views
# ----------------------------------------------------

class OrderList(APIView):
    """
    API view to list all orders or create a new order.

    GET: Returns a list of all orders.
    POST: Creates a new order with provided data.
    """
    def get(self, request):
        # Retrieve all orders from the database
        orders = Order.objects.all()
        # Serialize order data
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize and validate incoming order data
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Save new order to the database
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    """
    API view to retrieve, update, or delete an order instance.

    GET: Returns details of a specific order.
    PUT: Updates a specific order.
    DELETE: Deletes a specific order.
    """
    def get_object(self, pk):
        # Helper method to get order by primary key
        return Order.objects(id=pk).first()

    def get(self, request, pk):
        # Retrieve order instance
        order = self.get_object(pk)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        # Retrieve order instance
        order = self.get_object(pk)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Deserialize and validate incoming data
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            # Save updated order
            order = serializer.save()
            return Response(OrderSerializer(order).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Retrieve order instance
        order = self.get_object(pk)
        if not order:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Delete order
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# End of API Views
# ----------------------------------------------------

"""
Code Explanation:
- Each resource (User, Product, Order) has two API views: List (for GET/POST) and Detail (for GET/PUT/DELETE).
- List views handle listing all objects and creating new ones.
- Detail views handle retrieving, updating, and deleting a specific object by its primary key.
- Serializers are used for validation and serialization of data.
- HTTP status codes are used to indicate success or errors.
"""
