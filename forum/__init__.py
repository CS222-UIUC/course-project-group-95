from flask import Flask
from .views import user, post, index, message


# Flask factory mode to create the app
def create_app(test_config=None):

    # Declare html and css file location
    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./templates/static')

    app.config.from_mapping(SECRET_KEY='dev')

    # Declare database save location
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Register blueprint route
    app.register_blueprint(user.blueprint)
    app.register_blueprint(post.blueprint)
    app.register_blueprint(index.blueprint)
    app.register_blueprint(message.blueprint)
    # app.register_blueprint(views.blueprint)

    return app
