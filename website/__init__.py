from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
try:
    from .env import *
except:
    SECRET_KEY = os.getenv('SECRET_KEY')

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.debug = True
    db.init_app(app)
    
    from .views import home_view
    from .views import members_view
    from .views import members_2_view
    from .views import send_view
    from .views import messages_view
    from .views import thank_you_view
    
    app.register_blueprint(home_view, url_prefix='/')
    app.register_blueprint(members_view, url_prefix='/')
    app.register_blueprint(members_2_view, url_prefix='/')
    app.register_blueprint(send_view, url_prefix='/')
    app.register_blueprint(messages_view, url_prefix='/')
    app.register_blueprint(thank_you_view, url_prefix='/')
    
    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')