from flask import Flask
from app.routes.inventory_items import inventory_items
import logging

app = Flask(__name__)

app.register_blueprint(inventory_items)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start() -> None:
    logger.info("Initializing service")
    app.run(host="0.0.0.0", port=8888, debug=True)
    logger.info("Service finished initializing")
