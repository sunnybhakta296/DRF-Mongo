from rest_framework.test import APITestCase
from rest_framework import status
from api.models import User, Product

# Test case for User-related API endpoints
class UserTests(APITestCase):
    def test_create_user(self):
        """
        Test user creation via API.
        Sends a POST request to /api/users/ with user data.
        Asserts that the response status code is HTTP 201 CREATED.
        """
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "pass123"
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Test case for Product-related API endpoints
class ProductTests(APITestCase):
    def test_create_product(self):
        """
        Test product creation via API.
        Sends a POST request to /api/products/ with product data.
        Asserts that the response status code is HTTP 201 CREATED.
        """
        data = {
            "name": "Laptop",
            "description": "High-end gaming laptop",
            "price": 1999.99
        }
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
