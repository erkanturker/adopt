from flask import Flask,render_template,redirect,flash
from models import Pet,connect_db,db
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']="ekremAsimZehraErkan"

connect_db(app)
app.app_context().push()

@app.route("/")
def show_index():
    pets = Pet.query.all()
    return render_template("list_pets.html",pets=pets)

@app.route("/pets/new", methods=["GET","POST"])
def add_pets():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        available = form.available.data
        notes = form.notes.data

        new_pet = Pet(name=name,species=species, photo_url=photo_url,age=age,available=available,notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"{name} added as a new Pet")

        return redirect("/")
    else:
        return render_template('add_pet.html',form=form)
    
@app.route('/pets/<int:pet_id>/edit', methods=['GET','POST'])
def edit_pet(pet_id):
    
    updated_pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=updated_pet)

    if form.validate_on_submit():
        updated_pet.name = form.name.data
        updated_pet.species = form.species.data
        updated_pet.photo_url = form.photo_url.data
        updated_pet.age = form.age.data
        updated_pet.available = form.available.data
        updated_pet.notes = form.notes.data

        db.session.commit()

        flash(f"{updated_pet.name} is sucsesfully added")
        return redirect("/")
    else:
        return render_template("edit_pet.html",form=form)
    
@app.route("/pets/<int:pet_id>/delete")
def delete_pet(pet_id):
    pet  = Pet.query.get_or_404(pet_id)
    name = pet.name

    db.session.delete(pet)
    db.session.commit() 

    flash(f"{name} is succesfully deleted")
    return redirect("/")
        