from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,URL,Optional,NumberRange

from wtforms import StringField,URLField,IntegerField,BooleanField

class PetForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species",validators=[InputRequired()])
    photo_url = URLField("Phone Url",validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[Optional(),NumberRange(min=0)])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available", default=True)
