from ..models import User

import json
import datetime

HEADERS = {'Content-Type': 'application/json'}

def test_insert_and_retrieve_users(client,db):
    mock_user = User(
        name='John',
        date_of_birth=datetime.datetime.strptime('1997-03-30', '%Y-%m-%d').date(),
        email='john@gmail.com',
        country='Korea',
        city='Seoul',
        likes='good quality products',
        dislikes='none'
    )

    response = client.get('/users')
    assert len(response.get_json()['users']) == 0

    db.session.add(mock_user)

    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.get_json()['users']) == 1

    db.session.rollback()

def test_insert_users_bad_request(client):
    mock_data = {
        'name': 'Lisa',
        'date_of_birth': '03/09',
        'email': 'lisa@gmail.com',
        'country': 'Japan',
        'city': 'Tokyo',
        'likes': 'good quality products',
        'dislikes': 'none',
    }

    response = client.post('/users', data=json.dumps(mock_data), headers=HEADERS)
    assert response.status_code == 400

    mock_data['email'] = '@gmail.com'
    response = client.post('/users', data=json.dumps(mock_data), headers=HEADERS)
    assert response.status_code == 400