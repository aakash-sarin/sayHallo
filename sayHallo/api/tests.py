import pytest
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()
def make_request(query=""):
    return client.get(f"/api/hallo{query}")

def test_hallo_endpoint_with_name():
    response = make_request("?name=aakash")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"name": "aakash", "message": "Hallo aakash!"}

def test_hallo_endpoint_without_name():
    response = make_request()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "Missing 'name' parameter"}

def test_hallo_endpoint_with_empty_name():
    response = make_request()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "Missing 'name' parameter"}


