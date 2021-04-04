from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .. import app as _app, db as _db

import pytest
import os
import pathlib

TEST_DB_PATH = 'test_user.db'
TEST_DB_URI = f'sqlite:///{TEST_DB_PATH}'

# Configure app for testing
@pytest.fixture
def app():
    _app.config['TESTING'] = True
    _app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return _app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db(app,request):
    if os.path.exists(TEST_DB_PATH):
        os.unlink(os.path.join(TEST_DB_PATH))

    _db.app = app
    _db.create_all()

    @request.addfinalizer
    def teardown():
        _db.drop_all()
        os.unlink(os.path.join(pathlib.Path().absolute(),'user_feedback',TEST_DB_PATH))

    return _db