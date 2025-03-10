from flask import Flask
from flask_migrate import Migrate
from app.models.models import db
import os
from app.routes.inventory_items import inventory_items
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.register_blueprint(inventory_items)

app.config.from_mapping(
    {
        "SQLALCHEMY_DATABASE_URI": "mysql://user:password@127.0.0.1:3306/inventory_db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
)

db.init_app(app)
Migrate(app, db)


def start() -> None:
    logger.info("Initializing service")
    with app.app_context(): #Creacion del contexto de aplicacion
        db.create_all() #Creacion de tablas
        logger.info("Tables created.")
    app.run(host="0.0.0.0", port=8888, debug=True)
    logger.info("Service finished initializing")
    
