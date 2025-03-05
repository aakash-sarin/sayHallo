from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from rest_framework import status

def test_hallo_endpoint_with_name():
    client = APIClient()
    response = client.get("/api/hallo?name=John")
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"name": "John", "message": "Hallo John!"}

def test_hallo_endpoint_without_name():
    client = APIClient()
    response = client.get("/api/hallo")
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "Missing 'name' parameter"}

def test_hallo_endpoint_with_empty_name():
    client = APIClient()
    response = client.get("/api/hallo?name=")
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "Missing 'name' parameter"}


