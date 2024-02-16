from models import Pet,db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pets = [
    Pet(
        name="Fluffy",
        species="Cat",
        photo_url="https://media.istockphoto.com/id/1067347086/photo/cat-with-blue-eyes-looks-at-camera.webp?b=1&s=170667a&w=0&k=20&c=UvUyWWSKNX15YAuzQfsqeJholO_aRhRUU3QL-duqbWo=",
        age=3,
        notes="Likes to play with yarn",
        available=True
    ),
    Pet(
        name="Buddy",
        species="Dog",
        photo_url="https://img.freepik.com/free-photo/selective-focus-shot-adorable-golden-retriever-outdoors_181624-45215.jpg",
        age=2,
        notes="Very friendly and loves to fetch",
        available=True
    ),
    Pet(
        name="Whiskers",
        species="Cat",
        photo_url="https://hips.hearstapps.com/hmg-prod/images/beautiful-smooth-haired-red-cat-lies-on-the-sofa-royalty-free-image-1678488026.jpg?crop=0.668xw:1.00xh;0.119xw,0&resize=1200:*",
        age=5,
        notes="Enjoys napping in the sun",
        available=True
    ),
    Pet(
        name="Max",
        species="Dog",
        photo_url="https://static.vecteezy.com/system/resources/thumbnails/003/018/949/small/close-up-portrait-of-tricolor-australian-shepherd-dog-lying-on-the-table-of-a-natural-eye-park-around-him-free-photo.jpeg",
        age=4,
        notes="Loves long walks in the park",
        available=False
    ),
    Pet(
        name="Snowball",
        species="Rabbit",
        photo_url="https://cdn.pixabay.com/photo/2017/07/13/16/10/cute-2500929_640.jpg",
        age=1,
        notes="Loves carrots and hopping around",
        available=True
    ),
    Pet(
        name="Oreo",
        species="Guinea Pig",
        photo_url="https://thumbs.dreamstime.com/b/guinea-pig-over-white-373321.jpg",
        age=2,
        notes="Very cuddly and loves vegetables",
        available=True
    )
]

# Add the pets to the session and commit
db.session.add_all(pets)
db.session.commit()