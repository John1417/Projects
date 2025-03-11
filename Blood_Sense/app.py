from flask import Flask, render_template
from extensions.sql_alchemy import db, migrate
from setup_config import check_config, setup_config
from json import load

from blueprints.auth import auth_bp
from blueprints.specimen import specimen_bp
from blueprints.ml_models import  models_bp
from dashboard import create_dash_application

from flask_cors import CORS

def create_app():
    # need to setup varibales for database, secret key and more before running the application
    if not check_config():
        setup_config() # function to setup those variables

    # instantiate flask app
    app = Flask(__name__)

    # load configuration from config.json file created after calling setup_config() function
    app.config.from_file("config.json", load=load)

    # initialize dash app

    create_dash_application(app)
    
    # connect database

    db.init_app(app) # instantiate database
    migrate.init_app(app, db) # instantiate Flask-Migrate
    CORS(app) # instantiate cors


    # default index route
    # TODO: change this route to show login screens  
    @app.route("/", methods=["GET"])
    def homepage():
        return render_template("index.html")

    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(specimen_bp)
    app.register_blueprint(models_bp)

    # register dashboards

    return app


if __name__ == "__main__":
    # create application
    app = create_app()

    # run the application on port 7000
    # TODO: debug mode should be a swith, if enviornment is Production then debug should be 
    app.run(port=7000, debug=True)