from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, URL, NumberRange, AnyOf, Optional

class AddPetForm(FlaskForm):
    """
    Form for adding a new pet.
    """

    name = StringField(
        "Name",
        validators = [InputRequired(message="Please enter a name.")]
    )

    species = StringField(
        "Species",
        validators = [AnyOf(values=['cat', 'dog', 'porcupine'], message="Species must be dog, cat, or porcupine.")]
    )

    photo_url = StringField(
        "Photo URL",
        validators = [URL()]
    )

    age = IntegerField(
        "Age",
        validators = [NumberRange(min=0, max=30, message="Age must be between 0 and 30."), Optional()]
    )

    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """
    Form for editing pet details.
    """

    photo_url = StringField(
        "Photo URL",
        validators = [URL()]
    )

    notes = TextAreaField("Notes")

    available = BooleanField("Avaiable to adopt?")