from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sp4y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_pet_list():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('pets.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def show_pet_add_form():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.age.data

        Pet.add(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """
    Show pet details and a form to edit some of the details.
    On POST, handle any edits submitted from the form.
    """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        pet.edit(photo_url=photo_url, notes=notes, available=available)
        return redirect(f'/{pet_id}')
    else:
        return render_template('pet-details.html', form=form)