from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """
    A form for adding or editing pet information.

    Fields:
        name (StringField): The name of the pet. Required field.
        species (StringField): The species of the pet. Required field.
        photo_url (URLField): The URL of the pet's photo. Optional field.
        age (IntegerField): The age of the pet. Optional field.
        notes (StringField): Additional notes about the pet. Optional field.

    """
    name = StringField("Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    
    species = StringField("Species", validators=[
                        InputRequired(message="Species cannot be blank")])
    
    photo_url = URLField("Photo URL", validators=[URL(), Optional()])
    
    age = IntegerField("Age?", validators=[Optional()])
    
    notes = StringField("Notes", validators=[Optional()])
    
    
    