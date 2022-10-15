import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True,
            template_folder='./templates', static_folder='./templates/static')
app.config.from_mapping(SECRET_KEY='dev')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    from views import *
    app.register_blueprint(blueprint)

    app.run(debug=True)
