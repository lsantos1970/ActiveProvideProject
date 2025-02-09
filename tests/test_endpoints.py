import pytest
from app.routes import app

# Fixture para configurar o cliente de teste da aplicação Flask
@pytest.fixture
def client():
    """
    Configura o ambiente de teste para o Flask, permitindo simular solicitações HTTP.
    """
    app.testing = True  # Ativa o modo de teste para Flask
    return app.test_client()  # Retorna um cliente de teste

# Teste para o endpoint de configuração da atividade
def test_config_url(client):
    """
    Testa se o endpoint '/config_url' retorna um código de status HTTP 200 (OK).
    """
    response = client.get('/config_url')
    assert response.status_code == 200

# Teste para o endpoint de parâmetros JSON
def test_json_params_url(client):
    """
    Testa se o endpoint '/json_params_url' retorna um código de status HTTP 200 (OK).
    """
    response = client.get('/json_params_url')
    assert response.status_code == 200

# Teste para o endpoint de deployment de utilizadores
def test_user_url(client):
    """
    Testa se o endpoint '/user_url' retorna um código de status HTTP 200 (OK)
    ao passar um parâmetro de ID de instância.
    """
    response = client.get('/user_url?instanceID=12345')
    assert response.status_code == 200

# Teste para o endpoint de análise quantitativa e qualitativa
def test_analytics_url(client):
    """
    Testa se o endpoint '/analytics_url' retorna um código de status HTTP 200 (OK)
    ao enviar dados JSON válidos.
    """
    response = client.post('/analytics_url', json={"activityID": "12345"})
    assert response.status_code == 200

# Teste para o endpoint de lista de análises
def test_analytics_list_url(client):
    """
    Testa se o endpoint '/analytics_list_url' retorna um código de status HTTP 200 (OK).
    """
    response = client.get('/analytics_list_url')
    assert response.status_code == 200
