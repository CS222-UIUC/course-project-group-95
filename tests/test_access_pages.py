# from .__init__ import create_app
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from forum import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert (response.status_code == 200)
    assert response.data == b'Hello, World!'

def test_homepage(client):
    response = client.get('/')
    assert (response.status_code == 200)

def test_notification(client):
    response = client.get('/notification')
    assert (response.status_code == 200)

def test_profile(client):
    response = client.get('/profile')
    assert (response.status_code == 200)

def test_search(client):
    response = client.get('/search')
    assert (response.status_code == 200)