from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """
    A class defining a pet in the database.
    """

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    name = db.Column(
        db.Text,
        nullable = False
    )

    species = db.Column(
        db.Text,
        nullable = False
    )

    photo_url = db.Column(
        db.Text
    )

    age = db.Column(
        db.Integer
    )

    notes = db.Column(
        db.Text
    )

    available = db.Column(
        db.Boolean,
        default = True,
        nullable = False
    )

    @classmethod
    def add(cls, name, species, photo_url, age, notes):
        new_pet = cls(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

    def edit(self, photo_url, notes, available):
        self.photo_url = photo_url
        self.notes = notes
        self.available = available
        db.session.commit()
