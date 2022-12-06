from forum import create_app
from forum.db import db


# Call the factory build fuction to create the app and initialize the database
app = create_app()
db.init_app(app)


# When app.py is run, create database tables, and run the app in debug mode
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
