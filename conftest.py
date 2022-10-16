from forum import create_app
import pytest
from forum.db import db


@pytest.fixture
def app():
    app = create_app()
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
