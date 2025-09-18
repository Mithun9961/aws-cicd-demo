# test_application.py
from application import app  # Use your actual app file name

def test_homepage():
    """Test that the login page loads correctly"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login" in response.data  # Adjust to match your login page text

def test_login_success():
    """Test that valid login redirects to dashboard"""
    client = app.test_client()
    response = client.post(
        "/login",
        data=dict(email="hire-me@anshumat.org", password="HireMe@2025!"),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Dashboard" in response.data  # Adjust to your post-login page text

def test_login_fail():
    """Test that invalid login shows error"""
    client = app.test_client()
    response = client.post(
        "/login",
        data=dict(email="wrong@user.com", password="wrongpass"),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Invalid credentials" in response.data  # Adjust to your error message
