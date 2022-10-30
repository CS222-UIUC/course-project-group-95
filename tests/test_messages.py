from flask import get_flashed_messages, session
from forum.models.message import *
from forum.models.authentication import delete_all_user


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

    delete_all_post()
    delete_all_user()
