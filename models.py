from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    
    """
    A model class representing a pet potentially available for adoption.

    Attributes:
        id (int): An auto-incrementing unique identifier for the pet.
        name (str): The name of the pet.
        species (str): The species of the pet.
        photo_url (str): An optional URL to a photo of the pet.
        age (int): The age of the pet in years. Optional.
        notes (str): Additional notes about the pet. Optional.
        available (bool): Indicates whether the pet is currently available for adoption. Defaults to True.
    """
    
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    
    name = db.Column(db.String,
                     nullable = False)
    
    species = db.Column(db.String,
                        nullable = False)
    
    photo_url = db.Column(db.String) # add default photo?
    
    age = db.Column(db.Integer)
    
    notes = db.Column(db.String)
    
    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)