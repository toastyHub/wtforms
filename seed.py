"""Seed file to make sample data for db."""

from models import db, Pet
from app import app

waffle_img = 'https://images.unsplash.com/photo-1593483316242-efb5420596ca?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'

buggy_img = 'https://images.unsplash.com/photo-1537019575197-df34a13f342c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80'

pixel_img = 'https://images.unsplash.com/photo-1529257414772-1960b7bea4eb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'


# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

# Add sample pets
pet1 = Pet(name='Waffle', species='Cat', photo_url=waffle_img, age=4, notes='Waffle hates children')
pet2 = Pet(name='Buggy', species='Dog', photo_url=buggy_img, age=7, notes='The nicest doggy in the world')
pet3 = Pet(name='Pixel', species='Cat', photo_url=pixel_img, age=3, notes='Will destroy furniture')





db.session.add_all([pet1, pet2, pet3])
db.session.commit()


