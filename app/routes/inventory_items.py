from flask import Blueprint, request, render_template, redirect
from app.models.models import InventoryItem, db

inventory_items = Blueprint("inventory_items", __name__)


@inventory_items.route("/inventory_item")
def get_one():
    return "hello!"


@inventory_items.route("/")
def get_all():
    all_inventory_items = InventoryItem.query.all()
    return render_template("index.html", all_inventory_items=all_inventory_items)


@inventory_items.route("/add", methods=["POST"])
def create_one(session=db.session):
    new_inventory_item = InventoryItem(
        name=request.form["name"],
        price=request.form["price"],
        mac_address=request.form["mac_address"],
        serial_number=request.form["serial_number"],
        manufacturer=request.form["manufacturer"],
        description=request.form["description"],
    )
    session.add(new_inventory_item)
    session.commit()
    return redirect("/")


@inventory_items.route("/edit/<id>", methods=["GET", "POST"])
def update_one(session=db.session, id: int = 0):
    inventory_item = InventoryItem.query.get(id)
    if request.method == "POST":
        inventory_item.name = request.form["name"]
        inventory_item.price = request.form["price"]
        inventory_item.mac_address = request.form["mac_address"]
        inventory_item.serial_number = request.form["serial_number"]
        inventory_item.manufacturer = request.form["manufacturer"]
        inventory_item.description = request.form["description"]
        session.add(inventory_item)
        session.commit()
        session.refresh(inventory_item)
        return redirect("/")

    return render_template("test2.html", inventory_item=inventory_item)


@inventory_items.route("/delete/<id>")
def delete_one(session=db.session, id: int = 0):
    inventory_item = InventoryItem.query.get(id)
    if not inventory_item:
        return "Not found by id " + id
    session.delete(inventory_item)
    session.commit()
    return redirect("/")
