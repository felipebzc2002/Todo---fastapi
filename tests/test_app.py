from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    ESSE TESTE TEM 3 ETAPAS (AAA)

    - A: Arrange - Arranjo
    - A: ACT     - Chamar o bloco de teste (SUT)
    - A: ASSERT  - Garanta que A é A
    """

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola mundo'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'Felipe',
            'email': 'Felipe@gmail.com',
            'password': '123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Felipe',
        'email': 'Felipe@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Felipe',
                'email': 'Felipe@gmail.com',
                'id': 1,
            }
        ]
    }
