from flask import Blueprint, render_template, request, flash, jsonify
import json
from .mongo import *

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

@send_view.route('/send_message', methods=['GET', 'POST'])
def send_message():
    try:
        recipient = request.args.get('recipient')
        recipient = recipient.replace("_", " ")
        sender = request.args.get('sender')
        message = request.args.get('message')
        if [sender, message] in get_messages(collection, recipient):
            return json.dumps({'message': 'duplicate'})
        else:
            insert(collection, recipient, sender, message)
        response_data = {'message': 'success'}
        return json.dumps(response_data)
    except:
        response_data = {'message': 'error'}
        return json.dumps(response_data)

messages_view = Blueprint('messages_view', __name__)

@messages_view.route('/john_doe_00000', methods=['GET', 'POST'])
@messages_view.route(urls[0], methods=['GET', 'POST'])
@messages_view.route(urls[1], methods=['GET', 'POST'])
@messages_view.route(urls[2], methods=['GET', 'POST'])
@messages_view.route(urls[3], methods=['GET', 'POST'])
@messages_view.route(urls[4], methods=['GET', 'POST'])
@messages_view.route(urls[5], methods=['GET', 'POST'])
@messages_view.route(urls[6], methods=['GET', 'POST'])
@messages_view.route(urls[7], methods=['GET', 'POST'])
@messages_view.route(urls[8], methods=['GET', 'POST'])
@messages_view.route(urls[9], methods=['GET', 'POST'])
@messages_view.route(urls[10], methods=['GET', 'POST'])
@messages_view.route(urls[11], methods=['GET', 'POST'])
@messages_view.route(urls[12], methods=['GET', 'POST'])
@messages_view.route(urls[13], methods=['GET', 'POST'])
@messages_view.route(urls[14], methods=['GET', 'POST'])
@messages_view.route(urls[15], methods=['GET', 'POST'])
@messages_view.route(urls[16], methods=['GET', 'POST'])
@messages_view.route(urls[17], methods=['GET', 'POST'])
@messages_view.route(urls[18], methods=['GET', 'POST'])
@messages_view.route(urls[19], methods=['GET', 'POST'])
@messages_view.route(urls[20], methods=['GET', 'POST'])
@messages_view.route(urls[21], methods=['GET', 'POST'])
@messages_view.route(urls[22], methods=['GET', 'POST'])
@messages_view.route(urls[23], methods=['GET', 'POST'])
@messages_view.route(urls[24], methods=['GET', 'POST'])
@messages_view.route(urls[25], methods=['GET', 'POST'])
@messages_view.route(urls[26], methods=['GET', 'POST'])
@messages_view.route(urls[27], methods=['GET', 'POST'])
@messages_view.route(urls[28], methods=['GET', 'POST'])
@messages_view.route(urls[29], methods=['GET', 'POST'])
@messages_view.route(urls[30], methods=['GET', 'POST'])
@messages_view.route(urls[31], methods=['GET', 'POST'])
@messages_view.route(urls[32], methods=['GET', 'POST'])
@messages_view.route(urls[33], methods=['GET', 'POST'])
@messages_view.route(urls[34], methods=['GET', 'POST'])
@messages_view.route(urls[35], methods=['GET', 'POST'])
@messages_view.route(urls[36], methods=['GET', 'POST'])
@messages_view.route(urls[37], methods=['GET', 'POST'])
@messages_view.route(urls[38], methods=['GET', 'POST'])
@messages_view.route(urls[39], methods=['GET', 'POST'])
def home():
    name = request.path.split("/")[-1]
    name = name.replace("_", " ").title()
    name = name[:-5].strip()
    try:
        if name=="Ahmed El Basiouny":
            name = name.replace("B", "b")
    except:
        pass
    try:
        if name.startswith("Rana"):
            name = "Rana El-Ragabany"
    except:
        pass
    messages = []
    try:
        messages = get_messages(collection, name)
    except:
        pass
    return render_template('messages.html', messages=messages)

@messages_view.route('/expand', methods=['GET', 'POST'])
def expand():
    url = "/" + request.args.get('url')
    sender = request.args.get('sender')
    message = request.args.get('message')
    return render_template('message.html',url=url, sender=sender, message=message)

thank_you_view = Blueprint('thank_you_view', __name__)

@thank_you_view.route('/thank-you', methods=['GET', 'POST'])
def home():
    return render_template('thank-you.html')

stats_view = Blueprint('stats_view', __name__)

@stats_view.route('/stats', methods=['GET', 'POST'])
def home():
    num_of_msgs = number_of_messages(collection)
    return render_template('stats.html', num_of_msgs=num_of_msgs)