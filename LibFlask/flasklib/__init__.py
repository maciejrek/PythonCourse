from flask import Flask

app = Flask(__name__)

from flasklib import routes

app.config['SECRET_KEY'] = '4fff2e31bdb2baf9d1261d26833c6411'
