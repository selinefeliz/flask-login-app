import pytest
from main import app as flask_app # Importamos nuestra app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    """Un cliente de prueba para la aplicación."""
    return app.test_client()

def test_login_page_loads(client):
    """Prueba que la página de login carga correctamente."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Acceso de Usuario' in response.data # b'' indica bytes

def test_successful_authentication(client):
    """Prueba una autenticación exitosa."""
    response = client.post('/auth', data={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'success'

def test_failed_authentication_missing_data(client):
    """Prueba una autenticación fallida por falta de datos."""
    response = client.post('/auth', data={
        'email': 'test@example.com'
    })
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['status'] == 'error'

def test_failed_authentication_invalid_format(client):
    """Prueba una autenticación fallida por formato inválido."""
    response = client.post('/auth', data={
        'email': 'test@example.com',
        'password': 'short' # Menos de 8 caracteres
    })
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'formato inválido' in json_data['message']