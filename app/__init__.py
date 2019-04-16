from flask import Flask
import os, logging
from logging import Formatter
from logging.handlers import RotatingFileHandler

def create_app():
    app = Flask(__name__)

    logpath = os.path.join(os.getcwd(), 'sms_alert.log')
    handler = RotatingFileHandler(logpath, maxBytes=10485760, backupCount=4)
    formatter = Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    from main import main_blueprint
    app.register_blueprint(main_blueprint)

    return app