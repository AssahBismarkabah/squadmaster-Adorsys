# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()
# db object which we will use to interact with the database.


# create_app functiongiven a configuration name, loads the correct
# configuration from the config.py file, as well as the configurations
# from the instance/config.py file.
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You are not authorised to see this page. Please log in"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
