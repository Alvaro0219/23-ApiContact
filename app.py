from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Config de la bd
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
db = SQLAlchemy(app)

#Modelo de la app
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

    #Metodo para convertir objeto en tipo diccionario 
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

#Migrar modelos a la base de datos
with app.app_context():
    db.create_all()