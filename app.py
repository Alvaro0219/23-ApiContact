from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
db = SQLAlchemy(app)

# Modelo de la aplicación
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

    # Método para convertir objeto en tipo diccionario
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

# Migrar modelos a la base de datos
with app.app_context():
    db.create_all()

# Rutas

# Listar contactos
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify({"contacts": [contact.serialize() for contact in contacts]})

# Crear contactos
@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()

    # Validar campos obligatorios
    if 'name' not in data or 'email' not in data or 'phone' not in data:
        return jsonify({'error': 'Faltan campos obligatorios: name, email, phone'}), 400

    contact = Contact(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(contact)
    db.session.commit()

    return jsonify({"message": "Contacto creado con éxito", "contact": contact.serialize()}), 201

# Obtener contacto
@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({'error': 'No se encontró el contacto'}), 404
    
    return jsonify(contact.serialize())

# Editar contacto
@app.route('/contacts/<int:id>', methods=['PUT', 'PATCH'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)

    data = request.get_json()

    # Actualizar campos si existen en los datos
    if 'name' in data:
        contact.name = data['name']
    if 'email' in data:
        contact.email = data['email']
    if 'phone' in data:
        contact.phone = data['phone']

    db.session.commit()

    return jsonify({"message": "Contacto actualizado con éxito", "contact": contact.serialize()})

# Eliminar contacto
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({'error': 'No se encontró el contacto'}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contacto eliminado con éxito"})