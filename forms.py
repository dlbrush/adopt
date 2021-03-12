from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired

class AddPetForm(FlaskForm):
    """
    Form for adding a new pet or editing an existing pet.
    """

    name = StringField(
        "Name",
        validators=InputRequired()
    )

    species = StringField(
        "Species",
        validators=InputRequired()
    )

    photo_url = StringField("Photo URL")

    age = IntegerField("Age")

    notes = TextAreaField("Notes")