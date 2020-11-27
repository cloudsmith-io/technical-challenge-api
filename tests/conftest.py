import base64
import json
import pytest
from dotenv import load_dotenv

from challenge.models import User
from challenge.app import create_app
from challenge.extensions import db as _db
from pytest_factoryboy import register
from tests.factories import UserFactory


register(UserFactory)


@pytest.fixture(scope="session")
def app():
    load_dotenv(".testenv")
    app = create_app(testing=True)
    return app


@pytest.fixture
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def admin_user(db):
    user = User(
        username="admin",
        email="admin@admin.com",
        password="admin"
    )

    db.session.add(user)
    db.session.commit()

    return user


@pytest.fixture
def admin_headers(admin_user, client):
    auth = base64.b64encode(f"{admin_user.username}:{admin_user.password}".encode())
    return {
        "content-type": "application/json",
        "authorization": f"Basic {auth}"
    }
