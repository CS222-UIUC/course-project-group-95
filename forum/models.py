from app import db, app


class User(db.Model):

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password


def create_user(username, password):
    new_user = User(username, password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def delete_all_user():
    print(User.query.delete())
    db.session.commit()
    return "All user deleted."


def list_all_user():
    users = User.query.all()
    return users


if __name__ == "__main__":

    print("Creating database")
    with app.app_context():
        db.create_all()
    print("Database created successfully!")
