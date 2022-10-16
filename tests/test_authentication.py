from flask import get_flashed_messages
from forum.models.authentication import delete_all_user
import os


# Test server can handle get request to register.html
def test_register_page(client):
    response = client.get('/register.html')
    assert (response.status_code == 200)


# Test server can handle get request to login.html
def test_login(client):
    response = client.get('/login.html')
    assert (response.status_code == 200)


# Test server can handle get request to logout
def test_logout(client):
    response = client.get('/logout')
    assert (response.status_code == 302)


# Test register page can warn username not available
def test_register_no_username(client):
    response = client.post(
        '/register.html', data={'username': '', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Username is required.')


# Test register page can warn password not available
def test_register_no_password(client):
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Password is required.')


# Test register user
def test_register(client):
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    delete_all_user()


# Test register with existing username
def test_register_existing_user(client):
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Username exists.')
    os.remove("instance/forum.db")
