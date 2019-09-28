import pytest
from server.app import create_app

@pytest.fixture(scope="module")
def app():
    app = create_app()
    return app


def test_healthcheck(app):
    result = app.get('/')
    assert result.status_code == 200


