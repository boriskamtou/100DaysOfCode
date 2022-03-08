from flask import Flask, flash, jsonify, render_template, request
import random
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # Création de cette fonction pour la sérialisation
    def to_dict(self):
        dictionnary = {}
        for column in self.__table__.columns:
            dictionnary[column.name] = getattr(self, column.name)
        return dictionnary


@app.route("/")
def home():
    return render_template("index.html")


# Get random cafe
@app.route('/random')
def randomcafe():
    list_of_cafes = Cafe.query.all()
    random_cafe = random.choice(list_of_cafes)
    return jsonify(random_cafe.to_dict())

# HTTP GET - Read Record


@app.route('/all')
def all():
    list_of_cafes = Cafe.query.all()
    list_of_cafe_dict = []
    for cafe in list_of_cafes:
        list_of_cafe_dict.append(cafe.to_dict())
    return jsonify(cafes=list_of_cafe_dict)


@app.route('/search')
def search():
    query_location = request.args.get('location')
    list_of_cafe_at = Cafe.query.filter_by(location=query_location)
    if list_of_cafe_at != None:
        for cafe in list_of_cafe_at:
            list_of_cafe_at_dict = []
            list_of_cafe_at_dict.append(cafe.to_dict())
            return jsonify(cafes=list_of_cafe_at_dict)
    # Message d'erreur costomiser
    return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location."})

# HTTP POST - Create Record


@app.route('/add', methods=['POST'])
def add():
    # Un moyen d'ajouter des éléments à notre BD sans écrire un formulaire
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("loc"),
                    has_sockets=bool(request.form.get("sockets")),
                    has_toilet=bool(request.form.get("toilet")),
                    has_wifi=bool(request.form.get("wifi")),
                    can_take_calls=bool(request.form.get("calls")),
                    seats=request.form.get("seats"),
                    coffee_price=request.form.get("coffee_price"),)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()
    if cafe_to_update != None:
        new_price = request.args.get('update_price')
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully update the price"}), 200
    else:
        return jsonify(error={"Not found": "Sorry a coffee with that id was not found in the database"}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == 'TopSecretAPIKey':
        cafe_to_delete = Cafe.query.filter_by(id=cafe_id).first()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully delete the cafe"}), 200
        else:
            return jsonify(response={
                "error": "Sorry a coffee with that id was not found in the database"}), 404
    else:
        return jsonify(response={"Forbiden": "Your are not authorize to delete cafe in the database"}), 403


if __name__ == '__main__':
    app.run(debug=True)
