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
@messages_view.route('/abdelrahman_elnouty_21765', methods=['GET', 'POST'])
@messages_view.route('/abdelrahman_elsharabasy_89432', methods=['GET', 'POST'])
@messages_view.route('/abdulrahman_mohamed_50612', methods=['GET', 'POST'])
@messages_view.route('/ahmed_el_basiouny_73984', methods=['GET', 'POST'])
@messages_view.route('/ahmed_hany_12509', methods=['GET', 'POST'])
@messages_view.route('/ahmed_nabrawy_37492', methods=['GET', 'POST'])
@messages_view.route('/ahmed_el-khouly_82037', methods=['GET', 'POST'])
@messages_view.route('/ahmed_othman_16253', methods=['GET', 'POST'])
@messages_view.route('/alaa_dahshour_94510', methods=['GET', 'POST'])
@messages_view.route('/ali_fathy_30256', methods=['GET', 'POST'])
@messages_view.route('/ammar_azooz_67319', methods=['GET', 'POST'])
@messages_view.route('/amr_hazem_43870', methods=['GET', 'POST'])
@messages_view.route('/amr_salem_98124', methods=['GET', 'POST'])
@messages_view.route('/asmaa_el_goumri_36540', methods=['GET', 'POST'])
@messages_view.route('/ayman_mostafa_nagaty_72983', methods=['GET', 'POST'])
@messages_view.route('/bassel_elmaghrabi_50462', methods=['GET', 'POST'])
@messages_view.route('/dalia_elmessidy_12896', methods=['GET', 'POST'])
@messages_view.route('/fadi_nader_69502', methods=['GET', 'POST'])
@messages_view.route('/hassan_elarnaoudy_84719', methods=['GET', 'POST'])
@messages_view.route('/ingy_metwaly_20135', methods=['GET', 'POST'])
@messages_view.route('/mahmoud_metwally_54980', methods=['GET', 'POST'])
@messages_view.route('/marwan_gaber_76321', methods=['GET', 'POST'])
@messages_view.route('/medhat_osman_43056', methods=['GET', 'POST'])
@messages_view.route('/mohamed_elhabashy_98170', methods=['GET', 'POST'])
@messages_view.route('/mohamed_gamal_31245', methods=['GET', 'POST'])
@messages_view.route('/mohamed_helmy_87930', methods=['GET', 'POST'])
@messages_view.route('/mohamed_khamis_50413', methods=['GET', 'POST'])
@messages_view.route('/mohamed_mandour_17246', methods=['GET', 'POST'])
@messages_view.route('/mohamed_ramadan_69830', methods=['GET', 'POST'])
@messages_view.route('/mohamed_yassin_35492', methods=['GET', 'POST'])
@messages_view.route('/mohammed_balbaa_60783', methods=['GET', 'POST'])
@messages_view.route('/nesma_gaweesh_28941', methods=['GET', 'POST'])
@messages_view.route('/nouran_afify_70125', methods=['GET', 'POST'])
@messages_view.route('/nouran_el_gendy_94573', methods=['GET', 'POST'])
@messages_view.route('/omar_desouky_16240', methods=['GET', 'POST'])
@messages_view.route('/radwa_elsheikh_50792', methods=['GET', 'POST'])
@messages_view.route('/rana_el_ragabany_82146', methods=['GET', 'POST'])
@messages_view.route('/tamer_fares_43609', methods=['GET', 'POST'])
@messages_view.route('/wasim_magdy_29056', methods=['GET', 'POST'])
@messages_view.route('/yomna_el-raghy_71943', methods=['GET', 'POST'])
def home():
    name = request.path.split("/")[-1]
    name = name.replace("_", " ").title()
    name = name[:-5].strip()
    try:
        if name[9] == "B" and name[0] != "M":
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