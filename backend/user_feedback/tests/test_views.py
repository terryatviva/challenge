import json

HEADERS = {'Content-Type': 'application/json'}

def test_insert_and_retrieve_users(client):
    mock_data = {
        'name': 'John',
        'date_of_birth': '1997-03-30',
        'email': 'john@gmail.com',
        'country': 'Canada',
        'city': 'Toronto',
        'likes': 'good quality',
        'dislikes': 'none',
    }

    response = client.post('/users', data=json.dumps(mock_data), headers=HEADERS)
    assert response.status_code == 200

    response = client.get('/users')
    assert response.status_code == 200

def test_insert_users_bad_request(client):
    mock_data = {
        'name': 'Dawn',
        'date_of_birth': '03/09',
        'email': 'dawngmail.com',
        'country': 'Canada',
        'city': 'Toronto',
        'likes': 'dogs',
        'dislikes': 'cats',
    }

    response = client.post('/users', data=json.dumps(mock_data), headers=HEADERS)
    assert response.status_code == 400