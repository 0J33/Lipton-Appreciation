import os
import requests
try:
    from .env import *
except:
    GH_TOKEN = os.getenv("GH_TOKEN")
    GH_GIST_ID = os.getenv("GH_GIST_ID")

def read_gist(gist_id, file):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {GH_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        gist_data = response.json()
        files = gist_data["files"]
        return files[file + ".txt"]["content"]
    else:
        return "error"

def update_gist(content, gist_id, file):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {GH_TOKEN}"}
    data = {
        "files": {
            file + ".txt": {
                "content": content
            }
        }
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        return f"Gist updated: {gist_id}"
    else:
        return "error"