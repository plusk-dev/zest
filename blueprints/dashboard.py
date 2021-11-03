from flask import Blueprint, session, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from pony.orm import *
from models import Order
import calendar

dashboard_blueprint = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_blueprint.before_request
def before_request_func():
    if session.get("user") is None:
        return redirect(url_for("index"))


@dashboard_blueprint.get("/")
def index():
    return render_template("home.html")


@dashboard_blueprint.get("/estimate")
def estimate():
    return render_template("estimate.html")


@dashboard_blueprint.get("/types")
def types_of_window():
    return render_template("types.html")


@dashboard_blueprint.get("/order")
def order():
    order_id = request.args.get("id")
    with db_session:
        order = Order.get(id=order_id)
        return render_template("order.html", order=order)


@dashboard_blueprint.get("/all_orders")
def all_orders():
    with db_session:
        orders = select(o for o in Order).order_by(lambda o: o.date)
        print(list(orders))
        months = {}
        for i in orders:
            if i.date.strftime("%B %Y") not in months.keys():
                months[i.date.strftime("%B %Y")] = []
            months[i.date.strftime("%B %Y")].append(i)
        print(months)
        return render_template("all_orders.html", months=months)


@dashboard_blueprint.get("/profile")
def profile():
    return render_template("profile.html")


@dashboard_blueprint.get("/delete")
def delete_order():
    id = request.args.get("id")
    with db_session:
        order = Order.get(id=id)
        order.delete()
        return redirect(url_for("dashboard.all_orders"))


@dashboard_blueprint.get("/month_orders")
def month_orders():
    return render_template("monthly_audit.html")
