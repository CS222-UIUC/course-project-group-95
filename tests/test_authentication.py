from flask import get_flashed_messages, session
from forum.models.authentication import delete_all_user
import os


# Test server can handle get request to register.html
def test_register_page(client):
    response = client.get('/register.html')
    assert (response.status_code == 200)


# Test server can handle get request to login.html
def test_login_page(client):
    response = client.get('/login.html')
    assert (response.status_code == 200)


# Test server can handle get request to logout
def test_logout_page(client):
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


# Test login page can warn username not available
def test_login_no_username(client):
    response = client.post(
        '/login.html', data={'username': '', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Username is required.')


# Test login page can warn password not available
def test_login_no_password(client):
    response = client.post(
        '/login.html', data={'username': 'zhangsan', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Password is required.')


# Test login username not exist
def test_login_username_nonexist(client):
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/login.html', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "Username doesn't exist.")
    delete_all_user()


# Test login incorrect password
def test_login_password_incorrect(client):
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/login.html', data={'username': 'zhangsan', 'password': '12345'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "Password incorrect.")
    delete_all_user()


# Test login user and logout
def test_login_and_logout(client):
    assert (session.get('user_id') == None)
    response = client.post(
        '/register.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/login.html', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    assert (session.get('user_id') == 'zhangsan')
    response = client.get('/logout')
    assert (response.status_code == 302)
    assert (session.get('user_id') == None)
    delete_all_user()
