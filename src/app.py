"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "

    }
    
@app.route('/people', methods=['GET', 'POST'])
def handle_people():

    if request.body == 'POST':
        body = request.get.json()
        character = People(
            name=body['name'],
            height=body['height'],
            mass=body['mass'],
            hair_color=body['hair_color'],
            skin_color=body['skin_color'],
            eye_color=body['eye_color'],
            birth_year=body['birth_day'],
            gender=body['gender'],
            home_world=body['home_world']
        )
        db.session.add(character)
        db.session.commit()
        response_body = {
        "msg": "Character added correctly! "
    }
        return jsonify(response_body), 200

    if request.method == 'GET':
        all_people = People.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))
        responde_body = all_people
        return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
