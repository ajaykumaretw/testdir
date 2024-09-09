# test_app.py

from app import app

def test_home():
    # Use the Flask test client to send a GET request to the root URL
    response = app.test_client().get("/")
    
    # Check that the response status code is 200
    assert response.status_code == 200
    
    # Check that the response data matches the expected output with the exclamation mark
    assert response.data == b"Hello World!"  # Corrected assertion to match the actual response