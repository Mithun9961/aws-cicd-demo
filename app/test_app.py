# app/test_app.py

import pytest
from application import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage redirects to login page"""
    response = client.get("/", follow_redirects=True)
    assert response.status_code == 200
    # Check that the page contains "Login" form
    assert b"Login" in response.data or b"login" in response.data.lower()

def test_login_success(client):
    """Test login with correct credentials"""
    response = client.post(
        "/login",
        data=dict(email="hire-me@anshumat.org", password="HireMe@2025!"),
        follow_redirects=True
    )
    assert response.status_code == 200
    # Check that the page contains a welcome message or dashboard text
    assert b"Welcome" in response.data or b"dashboard" in response.data.lower()

def test_login_failure(client):
    """Test login with incorrect credentials"""
    response = client.post(
        "/login",
        data=dict(email="wrong@user.com", password="wrongpass"),
        follow_redirects=True
    )
    assert response.status_code == 200
    # Flexible check: the page should show some error related to invalid credentials
    error_texts = [b"invalid", b"wrong", b"error", b"credentials"]
    assert any(e in response.data.lower() for e in error_texts)
