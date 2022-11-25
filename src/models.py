from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favourites_id = db.Column(db.Integer, nullable=False)
    



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
        

  

class People(db.Model):
    __tablename__='people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(20), unique=False, nullable=False)
    skin_color = db.Column(db.String(20), unique=False, nullable=False)
    eye_color = db.Column(db.String(20),unique=False, nullable=False)
    birth_year = db.Column(db.String(20), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    home_world = db.Column(db.url_for, unique=False, nullable=False)
    # aqui irian direcciones de peliculas, vehiculos, naves,

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "home_world": self.home_world
        }

            # do not serialize the password, its a security breach

class Planets(db.models):
    __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_perior = db.Column(db.Integer, unique=false, nullable=False),
    orbital_perior = db.Column(db.Integer, unique=False, nullable=False),
    diameter = db.Column(db.Integer, unique=True, nullable=False),
    climate = db.Column(db.Integer, unique=True, nullable=False),
    gravity = db.Column(db.String(50), unique=True, nullable=False),
    terrain = db.Column(db.String(50), unique=True, nullable=False),
    surface_water = db.Column(db.Integer, unique=True, nullable=False),
    