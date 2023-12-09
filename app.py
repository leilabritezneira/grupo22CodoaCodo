"""La línea de comando:
pip install Flask SQLAlchemy mysql-connector-python 

se utiliza para instalar tres paquetes en tu entorno de Python. 
Aquí está una breve descripción de cada uno de ellos:

Flask: Flask es un framework ligero de desarrollo web para Python. Facilita la creación de aplicaciones web de manera rápida y sencilla. 
Con Flask, puedes definir rutas, gestionar solicitudes HTTP, y construir aplicaciones web de manera eficiente.

SQLAlchemy: SQLAlchemy es una biblioteca de SQL en Python que proporciona un conjunto de herramientas de alto nivel para interactuar con bases de datos relacionales. 
Facilita la creación, el acceso y la manipulación de bases de datos utilizando objetos Python en lugar de escribir directamente SQL.

mysql-connector-python: Este paquete es un conector oficial de MySQL para Python. Permite a tu aplicación Python conectarse y comunicarse con una base de datos MySQL. 
En el contexto de Flask y SQLAlchemy, se utiliza para establecer la conexión entre tu aplicación y la base de datos MySQL.

Marshmallow: Es una biblioteca de serialización/deserialización de objetos Python a/desde formatos como JSON.
Al importar estos módulos y clases, estamos preparando nuestro entorno de desarrollo para utilizar las funcionalidades que ofrecen. """

# 3. Importar las herramientas
# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy 

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow

# 4. Crear una instancia de la clase Flask con el nombre de la aplicación
app = Flask(__name__)

# Habilitar a la app para recibir peticiones, permitir el acceso desde el frontend al backend
CORS(app)

# 5. Configurar a la app la DB -> Configura la URI de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/db_23528'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)

# 6. Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)

# 7. Definir la tabla -> hereda de db.Model
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telefono = db.Column(db.String(50))

    def __init__(self, nombre, email, telefono):

        self.nombre = nombre
        self.email = email
        self.telefono = telefono

# 8. Crear la tabla al ejecutarse la app
with app.app_context():
    db.create_all()

# Crear ruta de acceso -> "/" es la ruta de inicio
@app.route("/")
def index():
    return f'App Web para registrar nombres de personas'

# Recibir los datos que vienen del formulario para insertarlos en la DB
@app.route("/registro", methods=['POST'])
def registro():
    nombre = request.json["nombre"]
    email = request.json["email"]
    telefono = request.json["telefono"]

    # ¿Cómo insertar el registro en la tabla?
    nuevo_registro = Persona(nombre, email, telefono) # Crea un nuevo objeto Persona con los datos proporcionados
    db.session.add(nuevo_registro) # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit() # Guarda los cambios en la base de datos

    return "Solicitud via post recibida"

# Retornar todos los registros de la tabla persona, en un Json
@app.route("/personas",  methods=['GET'])
def personas():
    # Consultar la tabla persona y traer todos los registros: all_registros -> lista de objetos
    all_registros = Persona.query.all()

    data_serializada = [] # Lista de diccionarios
    for registro in all_registros:
        data_serializada.append({"id":registro.id, "nombre":registro.nombre, "email":registro.email, "telefono":registro.telefono})

    # transformar a json
    return jsonify(data_serializada)

# Modificar un registro
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    # Buscar el registro por el id
    update_persona = Persona.query.get(id)

    # Recibir los nuevos datos a guardar
    nombre = request.json["nombre"]
    email = request.json["email"]
    telefono = request.json["telefono"]

    # Sobreescribir la info
    update_persona.nombre = nombre
    update_persona.email = email
    update_persona.telefono = telefono
    db.session.commit()

    data_serializada = [{"id": update_persona.id, "nombre": update_persona.nombre, "email": update_persona.email, "telefono": update_persona.telefono}]
    return jsonify(data_serializada)

# Eliminar una persona de la tabla persona por id
@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):
    # Buscar el registro por el id
    delete_persona = Persona.query.get(id)

    db.session.delete(delete_persona)
    db.session.commit()

    data_serializada = [{"id": delete_persona.id, "nombre": delete_persona.nombre, "email": delete_persona.email, "telefono": delete_persona.telefono}]
    return jsonify(data_serializada)

# Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)