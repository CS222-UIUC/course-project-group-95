from forum import create_app


# Test create_app success
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


# Test server can handle get request to hello
def test_hello(client):
    response = client.get('/hello')
    assert (response.status_code == 200)
    assert response.data == b'Hello, World!'


# Test server can handle get request to index page
def test_homepage(client):
    response = client.get('/')
    assert (response.status_code == 200)


# Test server can handle get request to message
def test_notification(client):
    response = client.get('/pm/message')
    assert (response.status_code == 200)


# Test server can handle get request to profile.html
def test_profile(client):
    response = client.get('/profile.html')
    assert (response.status_code == 200)
