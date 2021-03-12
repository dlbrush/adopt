from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

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
        redirect('/')
    else:
        render_template('add-pet.html', form=form)