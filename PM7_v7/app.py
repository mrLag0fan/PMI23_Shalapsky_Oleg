from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from  flask_marshmallow import Marshmallow
import os
import validdate


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Vaccination_Request(db.Model):

    vaccines = ["pfizer", "Moderna", "AstraZeneca"]#вакцини можуть бути тільки з цих і щоб не перевіряти на правильність написання назви вакцини ми вибираємо одну з них.
                                                   #якщо прийдеться додати нову ми просто записуємо в цей масив

    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), unique=True)
    patient_phone = db.Column(db.String(10))
    vaccine = db.Column(db.Integer)
    date = db.Column(db.String(10))
    start_time = db.Column(db.String(5))
    end_time = db.Column(db.String(5))

    def __init__(self, patient_name, patient_phone, vaccine_,
                 date_, start_time_, end_time_):
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine_
        self.date = date_
        self.start_time = start_time_
        self.end_time = end_time_



class Product_Schema(ma.Schema):
    class Meta:
        fields = ('id', 'patient_name', 'patient_phone', 'vaccine', 'date', 'start_time', 'end_time')

product_schema = Product_Schema()
products_schema = Product_Schema(many=True)


@app.route('/product', methods=["POST"])
def add_product():
    patient_name = request.json['patient_name']
    patient_phone = request.json['patient_phone']
    vaccine = request.json['vaccine']
    date = request.json['date']
    start_time = request.json['start_time']
    end_time = request.json['end_time']

    new_Product = Vaccination_Request(patient_name, patient_phone, vaccine, date, start_time, end_time)

    db.session.add(new_Product)
    db.session.commit()

    return product_schema.jsonify(new_Product)

@app.route('/product', methods=['GET'])
def get_products():
    all_products = Vaccination_Request.query.all()
    res = products_schema.dump(all_products)
    return jsonify(res)

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Vaccination_Request.query.get(id)
    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=["PUT"])
def updata_product(id):
    product = Vaccination_Request.query.get(id)

    patient_name = request.json['patient_name']
    patient_phone = request.json['patient_phone']
    vaccine = request.json['vaccine']
    date = request.json['date']
    start_time = request.json['start_time']
    end_time = request.json['end_time']

    product.patient_name = patient_name
    product.patient_phone = patient_phone
    product.vaccine = vaccine
    product.date = date
    product.start_time = start_time
    product.end_time = end_time

    db.session.commit()

    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Vaccination_Request.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

