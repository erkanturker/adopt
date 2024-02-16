from flask import Flask
from models import Pet,connect_db,db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']="ekremAsimZehraErkan"

connect_db(app)
app.app_context().push()

@app.route("/")
def show_index():
    return "Home page"