import pytest
from app.routes import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_config_url(client):
    response = client.get('/config_url')
    assert response.status_code == 200

def test_json_params_url(client):
    response = client.get('/json_params_url')
    assert response.status_code == 200

def test_user_url(client):
    response = client.get('/user_url?instanceID=12345')
    assert response.status_code == 200

def test_analytics_url(client):
    response = client.post('/analytics_url', json={"activityID": "12345"})
    assert response.status_code == 200

def test_analytics_list_url(client):
    response = client.get('/analytics_list_url')
    assert response.status_code == 200
