from models import db, Pet
from app import app

# Drop tables if they already exist, and then create them again
db.drop_all()
db.create_all()

# Delete all entries if there are any
Pet.query.delete()

# Create some pets
buddy = Pet(name="Buddy", species="Dog", age=3, notes="Hates birds", available=False, photo_url="https://images.unsplash.com/photo-1576201836106-db1758fd1c97?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80")
daphne = Pet(name="Daphne", species="Dog", age=5, photo_url="https://images.unsplash.com/photo-1529429617124-95b109e86bb8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80")
jim = Pet(name="Jim", species="Rabbit", age=2, notes="Scratch on his side", photo_url="https://images.unsplash.com/photo-1564650211163-21049f1b683a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1374&q=80")
hammy = Pet(name="Hammy", species="Hamster", age=1, photo_url="https://images.unsplash.com/photo-1425082661705-1834bfd09dca?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1355&q=80")
shadow = Pet(name="Shadow", species="Cat", age=8, available=False)

# Commit
db.session.add_all([buddy, daphne, jim, hammy, shadow])
db.session.commit()