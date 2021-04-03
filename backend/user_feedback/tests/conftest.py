import pytest

from .. import app

# Configure app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()