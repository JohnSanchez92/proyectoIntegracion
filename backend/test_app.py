import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'HOLA MUNDO' in response.data

def test_convertir_usd_a_mxn(client):
    response = client.post('/api/convertir', json={
        'cantidad': 100,
        'origen': 'USD',
        'destino': 'MXN'
    })
    assert response.status_code == 200
    assert response.json['resultado'] == 1700.0

def test_convertir_eur_a_usd(client):
    response = client.post('/api/convertir', json={
        'cantidad': 90,
        'origen': 'EUR',
        'destino': 'USD'
    })
    assert response.status_code == 200
    assert response.json['resultado'] == 100.0 

def test_moneda_invalida(client):
    response = client.post('/api/convertir', json={
        'cantidad': 50,
        'origen': 'XXX',
        'destino': 'USD'
    })
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Moneda no válida'
