from website import create_app
from flask import Flask
from threading import Thread

app = create_app()

def run():
  app.run(host='0.0.0.0',port=5000, use_reloader=False)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()