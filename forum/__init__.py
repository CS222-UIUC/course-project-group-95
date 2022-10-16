from flask import Flask
from .views import views


def create_app():

    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./templates/static')
    app.config.from_mapping(SECRET_KEY='dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

    app.register_blueprint(views.blueprint)

    return app
