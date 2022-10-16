from flask import Flask
from .views import views


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./templates/static')

    app.config.from_mapping(SECRET_KEY='dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(views.blueprint)

    return app
