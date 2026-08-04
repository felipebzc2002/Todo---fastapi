from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():

    '''
    ESSE TESTE TEM 3 ETAPAS (AAA)

    - A: Arrange - Arranjo
    - A: ACT     - Chamar o bloco de teste (SUT)
    - A: ASSERT  - Garanta que A é A
    '''

    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo'}
    assert response.status_code == HTTPStatus.OK
