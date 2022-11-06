from flask import get_flashed_messages, session
from forum.models.authentication import delete_all_user


# Test server can handle get request to register.html
def test_register_page(client):
    response = client.get('/user/register')
    assert (response.status_code == 200)


# Test server can handle get request to login.html
def test_login_page(client):
    response = client.get('/user/login')
    assert (response.status_code == 200)


# Test server can handle get request to logout
def test_logout_page(client):
    response = client.get('/user/logout')
    assert (response.status_code == 302)


# Test register page can warn username not available
def test_register_no_username(client):
    response = client.post(
        '/user/register', data={'username': '', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Username is required.')


# Test register page can warn password not available
def test_register_no_password(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Password is required.')


# Test register user
def test_register(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    delete_all_user()


# Test register with existing username
def test_register_existing_user(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Username exists.')
    delete_all_user()


# Test login page can warn username not available
def test_login_no_username(client):
    response = client.post(
        '/user/login', data={'username': '', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Username is required.')


# Test login page can warn password not available
def test_login_no_password(client):
    response = client.post(
        '/user/login', data={'username': 'zhangsan', 'password': ''})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == 'Password is required.')


# Test login username not exist
def test_login_username_nonexist(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/user/login', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "Username doesn't exist.")
    delete_all_user()


# Test login incorrect password
def test_login_password_incorrect(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/user/login', data={'username': 'zhangsan', 'password': '12345'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "Password incorrect.")
    delete_all_user()


# Test login user and logout
def test_login_and_logout(client):
    assert (session.get('user_id') == None)
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/user/login', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    assert (session.get('user_id') == 'zhangsan')
    response = client.get('/user/logout')
    assert (response.status_code == 302)
    assert (session.get('user_id') == None)
    delete_all_user()


# Test list all users
def test_list_all_users(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    response = client.post(
        '/user/register', data={'username': 'lisi', 'password': '123'})
    response = client.get('/user/list')
    assert (response.data == b'["zhangsan","lisi"]\n')

    response = client.get('user/clean')
    assert (response.status_code == 200)

    response = client.get('/user/list')
    assert (response.data == b'[]\n')
