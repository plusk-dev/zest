from flask import Flask, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from blueprints import auth_blueprint, dashboard_blueprint, estimate_api_blueprint
from models.main import User, database
from pony.orm import db_session, select
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(estimate_api_blueprint)
app.config["SECRET_KEY"] = "add50c38-0102-4490-83bf-c08f56a8f66a"
app.config['JSON_SORT_KEYS'] = False


@app.before_first_request
def handle_startup():
    # if app.debug == True:
    #     database.bind("sqlite", "database.sqlite", create_db=True)
    # elif app.debug == False:
    #     database.bind(provider='postgres', user='vjxssxtaunspvh', password='b2b8dd9ab9400ca06ad2045cb9fb808b9d077ce6d514474ead7d7d058436ab3e',
    #                   host='ec2-3-228-134-188.compute-1.amazonaws.com', database='d264r6pqscns36')

    database.bind("sqlite", "database.sqlite", create_db=True)
    database.generate_mapping(create_tables=True)
    try:
        with db_session:
            u = User(username="zestadmin", password="zestadmin82008",
                     display_name="administrator", admin=True)
            print(list(select(p for p in User)))
    except Exception as e:
        print(e)


@app.get("/")
def index():
    return redirect(url_for("auth.login_page"))


if __name__ == "__main__":
    app.run(debug=False, port=5000)
    # app.run(host="0.0.0.0")
