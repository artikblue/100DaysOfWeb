from apistar import test

from app import app, connections, CON_NOT_FOUND

client = test.TestClient(app)
# SOME BASIC TESTS TO PLAY WITH PYTEST
def test_list_connections():
    response = client.get('/')
    assert response.status_code == 200

    json_resp = response.json()
    con_count = len(connections)
    assert len(json_resp) == con_count

    expected = {"id":1,"user_agent":"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6","country":"Mexico","date":"1/20/2019","ipv4_addr":"164.224.54.120"}

    assert json_resp[0] == expected

def test_create_con():
    con_count = len(connections)
    data = {"user_agent":"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6","country":"Mexico","date":"1/20/2019","ipv4_addr":"124.224.11.3"}

    response = client.post('/', data=data)
    assert response.status_code == 201
    assert len(connections) == con_count + 1

    response = client.get('/1001/')
    expected = {"id":1001,"user_agent":"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6","country":"Mexico","date":"1/20/2019","ipv4_addr":"124.224.11.3"}

    assert response.json() == expected

def test_create_con_missing_fields():
    data = {'key': 1}
    response = client.post('/', data=data)
    assert response.status_code == 400

    errors = response.json()

    assert errors['user_agent'] == 'The "user_agent" field is required.'
    assert errors['country'] == 'The "country" field is required.'
    assert errors['ipv4_addr'] == 'The "ipv4_addr" field is required.'
    assert errors['date'] == 'The "date" field is required.'

def test_create_con_field_validation():
    data = {"user_agent":"M"*700,"country":"Mexico","date":"1/20/2019","ipv4_addr":"124.224.11.3"}

    response = client.post('/', data=data)
    assert response.status_code == 400

    errors = response.json()
    assert errors['user_agent'] == 'Must have no more than 300 characters.'
