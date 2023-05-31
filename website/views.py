from flask import Blueprint, render_template, request, flash, jsonify
from . import db
import json
from .git_func import *

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
        content = recipient + "/////" + sender + "/////" + message + "\n"
        old = read_gist(GH_GIST_ID, "lipton_appreciation")
        update_gist(old + content, GH_GIST_ID, "lipton_appreciation")
        return "success"
    except:
        return "error"

messages_view = Blueprint('messages_view', __name__)

@messages_view.route('/abdelrahman_elnouty_21765', methods=['GET', 'POST'])
@messages_view.route('/abdelrahman_elsharabasy_89432', methods=['GET', 'POST'])
@messages_view.route('/abdulrahman_mohamed_50612', methods=['GET', 'POST'])
@messages_view.route('/ahmed_el_basiouny_73984', methods=['GET', 'POST'])
@messages_view.route('/ahmed_hany_12509', methods=['GET', 'POST'])
@messages_view.route('/ahmed_hassan_37492', methods=['GET', 'POST'])
@messages_view.route('/ahmed_mahmoud_82037', methods=['GET', 'POST'])
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
@messages_view.route('/hassan_youssef_84719', methods=['GET', 'POST'])
@messages_view.route('/ingy_metwaly_20135', methods=['GET', 'POST'])
@messages_view.route('/mahmoud_mohamed_54980', methods=['GET', 'POST'])
@messages_view.route('/marwan_mohamed_76321', methods=['GET', 'POST'])
@messages_view.route('/medhat_osman_43056', methods=['GET', 'POST'])
@messages_view.route('/mohamed_elhabashy_98170', methods=['GET', 'POST'])
@messages_view.route('/mohamed_gamal_31245', methods=['GET', 'POST'])
@messages_view.route('/mohamed_helmy_87930', methods=['GET', 'POST'])
@messages_view.route('/mohamed_khamis_50413', methods=['GET', 'POST'])
@messages_view.route('/mohamed-mandour_17246', methods=['GET', 'POST'])
@messages_view.route('/mohamed_ramadan_69830', methods=['GET', 'POST'])
@messages_view.route('/mohamed_yassin_35492', methods=['GET', 'POST'])
@messages_view.route('/mohammed_balbaa_60783', methods=['GET', 'POST'])
@messages_view.route('/nesma_gaweesh_28941', methods=['GET', 'POST'])
@messages_view.route('/nouran_afify_70125', methods=['GET', 'POST'])
@messages_view.route('/nouran_el_gendy_94573', methods=['GET', 'POST'])
@messages_view.route('/omar_desouky_16240', methods=['GET', 'POST'])
@messages_view.route('/radwa_mahmoud_50792', methods=['GET', 'POST'])
@messages_view.route('/rana_ossama_82146', methods=['GET', 'POST'])
@messages_view.route('/tamer_fares_43609', methods=['GET', 'POST'])
@messages_view.route('/wasim_magdy_29056', methods=['GET', 'POST'])
@messages_view.route('/yomna_el-raghby_71943', methods=['GET', 'POST'])
def home():
    name = request.path.split("/")[-1]
    name = name.replace("_", " ").title()
    name = name[:-5].strip()
    messages = []
    try:
        data = read_gist(GH_GIST_ID, "lipton_appreciation")
        all_messages = data.split("\n")
        for message in all_messages:
            if name in message.split("/////")[0]:
                message = message.strip()
                message = message.split("/////")
                messages.append([message[1], message[2]])
    except:
        pass
    return render_template('messages.html', messages=messages)

thank_you_view = Blueprint('thank_you_view', __name__)

@thank_you_view.route('/thank-you', methods=['GET', 'POST'])
def home():
    return render_template('thank-you.html')