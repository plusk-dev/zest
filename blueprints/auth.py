from flask import Blueprint, request, session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from models.main import User
from pony.orm import db_session

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

credentials = {
    "username": "admin",
    "password": "password"
}


@auth_blueprint.get("/")
def login_page():
    if session.get("user") is not None:
        return redirect(url_for("dashboard.index"))
    return render_template("login.html")


def authenticate(data: dict) -> bool:
    with db_session:
        user = User.get(username=data.get('username'))
        if user is not None and user.password == data.get('password'):
            return user
        return None


@auth_blueprint.post("/login")
def login():
    form_data = request.form.to_dict()
    user = authenticate(form_data)
    if user is not None:
        user_data = user.to_dict()
        user_data.pop("password")
        session["user"] = user_data
        return redirect(url_for("dashboard.index"))
    else:
        return redirect(url_for("index"))


@auth_blueprint.get("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("index"))