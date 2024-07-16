from flask import Flask

# Importar las configuraciones y funciones necesarias
import requests
from requests.auth import HTTPBasicAuth

##############################
SURREALDB_URL           = "http://127.0.0.1:8000/sql"
SURREALDB_NAMESPACE     = "SurrealDBPython"
SURREALDB_DATABASE_NAME = "root"
SURREALDB_USER_NAME     = "root"
SURREALDB_USER_PASSWORD = "root"

##############################
def db(query):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'ns': SURREALDB_NAMESPACE,
        'db': SURREALDB_DATABASE_NAME
    }
    r = requests.post(SURREALDB_URL,
                      data=query,
                      headers=headers,
                      auth=HTTPBasicAuth(SURREALDB_USER_NAME, SURREALDB_USER_PASSWORD))
    if "code" in r.json():
        raise Exception(r.json())
    return r.json()

def create_app():
    app = Flask(__name__)

    # Configurar la clave secreta de Flask
    app.config['SECRET_KEY'] = 'mi_clave_secreta_aqui'

    # Importar y registrar las rutas
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
