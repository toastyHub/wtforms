from flask import Flask, request, redirect, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "toasty"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

### HOME ROUTE ###################################################################
@app.route('/')
def list_pets():
    """Route to list all pets in the database.

    Returns:
        A rendered template of 'index.html' displaying all the pets.
    """
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

### FORM ROUTES #################################################################
@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Route to add a new pet to the database.

    Returns:
        If the form is validated, redirects to the homepage. 
        Otherwise, renders the 'add-pet.html' template with the add pet form.
    """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """
    Edit an existing pet record in the database.

    Args:
        pet_id (int): The ID of the pet to be edited.

    Returns:
        If the form is submitted and valid, redirects to the home page.
        Otherwise, renders the edit-pet template with the form and pet data.

    """
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        Pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
    
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit-pet.html', form=form, pet=pet)
