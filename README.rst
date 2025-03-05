=================================
sayHallo
=================================

The projected was created to demostrate a GET endpoint in Django that returns "Hallo".

Project Setup
------------------------------

1. Clone the Repository::

    git clone https://github.com/aakash-sarin/sayHallo.git
    cd sayHallo

2. Create and Activate Virtual Environment::

    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies::

    pip install -r requirements.txt

Running the Project
------------------------------

Start the Django development server::

    python manage.py runserver

The API should now be accessible at::

    http://127.0.0.1:8000/api/hallo

Testing the API
------------------------------

Using ``curl``:

- **Valid Request**::

    curl -X GET "http://127.0.0.1:8000/api/hallo?name=aakash"

  **Response:**
  
  .. code-block:: json

      {
          "name": "aakash",
          "message": "Hallo aakash!"
      }

- **Missing `name` Parameter**::

    curl -X GET "http://127.0.0.1:8000/api/hallo"

  **Response:**
  
  .. code-block:: json

      {
          "error": "Missing 'name' parameter"
      }

- **Empty `name` Parameter**::

    curl -X GET "http://127.0.0.1:8000/api/hallo?name="

  **Response:**
  
  .. code-block:: json

      {
          "error": "Missing 'name' parameter"
      }

Running Tests
------------------------------

To execute test cases, run::

    pytest -v

Expected output::

    test_hallo_endpoint_with_name PASSED
    test_hallo_endpoint_without_name PASSED
    test_hallo_endpoint_with_empty_name PASSED

