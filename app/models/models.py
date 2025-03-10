from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric

db = SQLAlchemy()


class InventoryItem(db.Model):
    __tablename__ = "inventory_item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(Numeric(10, 2), nullable=False)
    mac_address = db.Column(db.String(150), nullable=False)
    serial_number = db.Column(db.String(150), nullable=False)
    manufacturer = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __init__(
        self, name, price, mac_address, serial_number, manufacturer, description
    ):
        self.name = name
        self.price = price
        self.mac_address = mac_address
        self.serial_number = serial_number
        self.manufacturer = manufacturer
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "mac_address": self.mac_address,
            "serial_number": self.serial_number,
            "manufacturer": self.manufacturer,
            "description": self.description,
        }
