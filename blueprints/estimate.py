from datetime import datetime
from flask import Blueprint, request
from flask.json import jsonify
from compute import compute_material_required
from pony.orm import *
from models import User
import json
import pytz
from models.main import Order



estimate_api_blueprint = Blueprint(
    "estimate", __name__, url_prefix="/estimate")
IST = pytz.timezone('Asia/Kolkata')


@estimate_api_blueprint.get("/")
def estimate():
    width = request.args.get("width")
    height = request.args.get("height")
    return jsonify(compute_material_required(width=float(width), height=float(height)))


@estimate_api_blueprint.post("/create_order")
def create_order():
    request_data = json.loads(request.data.decode('utf8').replace("'", '"'))
    print(request_data)
    order_name = request_data.get("name")
    username = request_data.get("username")
    password = request_data.get("password")
    order_data = request_data.get("order_data")
    with db_session:
        user = User.get(username=username, password=password)
        if user is not None:
            order = Order(name=order_name,
                          date=datetime.now(IST), data=order_data)
            return jsonify({
                "message": "ok",
                "order_data": order.to_dict()
            })
        return jsonify({
            "message": "error"
        })


def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


@estimate_api_blueprint.post("/month_orders")
def month_orders():
    month = request.args.get("month")
    year = request.args.get("year")
    with db_session:
        orders = select(o for o in Order if o.date.month ==
                        month_string_to_number(month) and o.date.year == int(year)).order_by(lambda o: o.date)
        order_dict = {}
        order_dict["orders"] = []
        for i in orders:
            order_dict["orders"].append(i.to_dict())
        return order_dict
