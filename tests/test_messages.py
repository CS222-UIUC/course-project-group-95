from flask import get_flashed_messages, session
from forum.models.message import delete_all_pm
from forum.models.authentication import delete_all_user


# Test add connection function
def test_add_connection(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    response = client.post(
        '/user/login', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    response = client.post(
        '/user/register', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 302)
    response = client.get('/pm/message')
    assert (response.status_code == 200)
    response = client.get('/pm/connection_management')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'username': 'nomatch'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "No matching result")
    response = client.post(
        '/pm/connection_management', data={'username': 'lisi'})
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'send_connection': 'lisi'})
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'send_connection': 'lisi'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "Connection request already exist")
    response = client.get('/user/logout')
    assert (response.status_code == 302)
    response = client.post(
        '/user/login', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 302)
    response = client.get('/pm/message')
    assert (response.status_code == 200)
    response = client.get('/pm/connection_management')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'decline_connection': 'zhangsan'})
    assert (response.status_code == 200)
    response = client.get('/user/logout')
    assert (response.status_code == 302)
    response = client.post(
        '/user/login', data={'username': 'zhangsan', 'password': '123'})
    response = client.get('/pm/message')
    assert (response.status_code == 200)
    response = client.get('/pm/connection_management')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'username': 'lisi'})
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'send_connection': 'lisi'})
    assert (response.status_code == 200)
    response = client.get('/user/logout')
    assert (response.status_code == 302)
    response = client.post(
        '/user/login', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 302)
    response = client.get('/pm/message')
    assert (response.status_code == 200)
    response = client.get('/pm/connection_management')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'accept_connection': 'zhangsan'})
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'delete_connection': 'zhangsan'})
    assert (response.status_code == 200)

    delete_all_pm()
    delete_all_user()


# Test private message function
def test_private_message(client):
    response = client.post(
        '/user/register', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    response = client.post(
        '/user/login', data={'username': 'zhangsan', 'password': '123'})
    assert (response.status_code == 302)
    response = client.post(
        '/user/register', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 302)
    response = client.get('/pm/message')
    assert (response.status_code == 200)
    response = client.get('/pm/connection_management')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'username': 'lisi'})
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'send_connection': 'lisi'})
    assert (response.status_code == 200)
    response = client.get('/user/logout')
    assert (response.status_code == 302)
    response = client.post(
        '/user/login', data={'username': 'lisi', 'password': '123'})
    assert (response.status_code == 302)
    response = client.get('/pm/message')
    assert (response.status_code == 200)
    response = client.get('/pm/connection_management')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/connection_management', data={'accept_connection': 'zhangsan'})
    assert (response.status_code == 200)
    response = client.get(
        '/pm/message?conversation=zhangsan')
    assert (response.status_code == 200)
    response = client.post(
        '/pm/message?conversation=zhangsan', data={'content': 'This is a private message'})
    assert (response.status_code == 200)
    response = client.get(
        '/pm/message?conversation=zhangsan')
    assert (response.status_code == 200)

    delete_all_pm()
    delete_all_user()
