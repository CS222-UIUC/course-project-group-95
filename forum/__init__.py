import os

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./templates/static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/notification')
    def notification():
        return render_template('notification.html')

    @app.route('/profile')
    def profile():
        return render_template('profile.html')

    @app.route('/search')
    def search():
        return render_template('search.html')

    return app
