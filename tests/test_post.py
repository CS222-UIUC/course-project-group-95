from flask import get_flashed_messages, session
from forum.models.post import *
from forum.models.authentication import delete_all_user
import os


# Test create_post function
def test_create_post(client):
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
    response = client.post(
        '/post/create', data={'title': '', 'content': 'no title'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages[0] == "Title is required.")
    response = client.post(
        '/post/create', data={'title': 'post title', 'content': 'this is a post'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/post/create', data={'title': 'post title2', 'content': 'this is another post'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.get('/')
    assert (response.status_code == 200)
    posts = list_all_posts()
    assert (posts[1].title == 'post title')
    assert (posts[1].content == 'this is a post')
    assert (posts[0].title == 'post title2')
    assert (posts[0].content == 'this is another post')
    check_only_two_posts = False
    try:
        post = posts[2]
    except:
        check_only_two_posts = True
    assert (check_only_two_posts)

    delete_all_user()
    delete_all_post()


# Test edit_post function
def test_edit_post(client):
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
    response = client.post(
        '/post/create', data={'title': 'post title', 'content': 'this is a post'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    response = client.post(
        '/post/edit?id=1', data={'title': '', 'content': 'no title'})
    assert (response.status_code == 200)
    messages = get_flashed_messages()
    assert (messages == ['Title is required.'])
    response = client.post(
        '/post/edit?id=1', data={'title': 'post title edit', 'content': 'this is an edited post'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])

    delete_all_user()
    delete_all_post()


# Test view_and_delete_post function
def test_view_and_delete_post(client):
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
    response = client.post(
        '/post/create', data={'title': 'post title', 'content': 'this is a post'})
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    post = get_post(1)
    assert (post.title == 'post title')
    assert (post.content == 'this is a post')
    response = client.get('/post/view?id=1')
    assert (response.status_code == 200)
    response = client.get(
        '/post/delete?id=1')
    assert (response.status_code == 302)
    messages = get_flashed_messages()
    assert (messages == [])
    posts = list_all_posts()
    check_empty = False
    try:
        post = posts[0]
    except:
        check_empty = True
    assert (check_empty)

    delete_all_user()
    delete_all_post()
