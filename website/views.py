from flask import Blueprint, render_template, request, flash, jsonify
from . import db
import json
from .messages import *

home_view = Blueprint('home_view', __name__)

@home_view.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

members_view = Blueprint('members_view', __name__)

@members_view.route('/members', methods=['GET', 'POST'])
def home():
    return render_template('members.html')

members_2_view = Blueprint('members_2_view', __name__)

@members_2_view.route('/members-2', methods=['GET', 'POST'])
def home():
    return render_template('members-2.html')

send_view = Blueprint('send_view', __name__)

@send_view.route('/send', methods=['GET', 'POST'])
def home():
    name = request.args.get('name')
    return render_template('send.html', recipient=name)

messages_view = Blueprint('messages_view', __name__)

# first name last name random 5 digits
@messages_view.route('/abdelrahman-elnouty-21765', methods=['GET', 'POST'])
@messages_view.route('/abdelrahman-elsharabasy-89432', methods=['GET', 'POST'])
def home():
    return render_template('messages.html')

thank_you_view = Blueprint('thank_you_view', __name__)

@thank_you_view.route('/thank-you', methods=['GET', 'POST'])
def home():
    return render_template('thank-you.html')