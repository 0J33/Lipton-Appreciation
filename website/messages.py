import os
try:
    from .env import *
except:
    GH_TOKEN = os.getenv("GH_TOKEN")
    GH_GIST_ID = os.getenv("GH_GIST_ID")
from .git_func import *

def send_message(recipient, sender, message):
    recipient = recipient.strip()
    sender = sender.strip()
    message = message.strip()
    data = recipient + "/////" + sender + "/////" + message + "\n"
    old = read_gist(GH_GIST_ID, "lipton_appreciation")
    print(old + data)
    update_gist(old + data, GH_GIST_ID, "lipton_appreciation")

def get_messages(name):
    data = read_gist(GH_GIST_ID, "lipton_appreciation.txt")
    # format: recipient/////sender/////message
    all_messages = data.split("\n")
    messages = []
    for message in all_messages:
        if name in message.split("/////")[0]:
            message = message.strip()
            message = message.split("/////")
            messages.append([message[1], message[2]])
    return messages