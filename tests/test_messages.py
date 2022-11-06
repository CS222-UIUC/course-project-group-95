from flask import get_flashed_messages, session
from forum.models.message import delete_all_pm
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
    # add_connection('zhangsan', 'lisi')
    # response = client.get(
    #     '/pm/message?conversation=lisi')
    # assert (response.status_code == 200)
    # response = client.post(
    #     '/pm/message?conversation=lisi', data={'content': 'This is a private message'})
    # assert (response.status_code == 200)
    # response = client.get(
    #     '/pm/message?conversation=lisi')
    # assert (response.status_code == 200)

    delete_all_pm()
    delete_all_user()
