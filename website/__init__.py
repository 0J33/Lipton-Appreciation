from flask import Flask
import os
from pymongo import MongoClient

try:
    from .env import *
except:
    SECRET_KEY = os.getenv('SECRET_KEY')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.debug = True
    
    from .views import home_view
    from .views import members_view
    from .views import members_2_view
    from .views import send_view
    from .views import messages_view
    from .views import thank_you_view
    from .views import stats_view
    
    app.register_blueprint(home_view, url_prefix='/')
    app.register_blueprint(members_view, url_prefix='/')
    app.register_blueprint(members_2_view, url_prefix='/')
    app.register_blueprint(send_view, url_prefix='/')
    app.register_blueprint(messages_view, url_prefix='/')
    app.register_blueprint(thank_you_view, url_prefix='/')
    app.register_blueprint(stats_view, url_prefix='/')

    return app