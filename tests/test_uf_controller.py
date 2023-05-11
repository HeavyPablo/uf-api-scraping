def test_get_uf_today(client):
    response = client.get('/uf')

    assert 'data' in response.json


def test_get_uf_from_date(client):
    response = client.get('/uf?date=2022-01-05')

    assert 'data' in response.json


def test_get_error_from_date_not_register_uf(client):
    response = client.get('/uf?date=2024-04-01')

    assert 'error' in response.json


