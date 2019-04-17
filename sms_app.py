#!/usr/bin/env python3
from flask import Flask, request, jsonify, json
from logging import Formatter
from logging.handlers import RotatingFileHandler
import os, logging

app = Flask(__name__)

logpath = os.path.join(os.getcwd(), 'sms_alert.log')
handler = RotatingFileHandler(logpath, maxBytes=10485760, backupCount=4)
formatter = Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# send sms alert
def alert(text):
    print(text)

# it's called by ops lambda to check server health
@app.route('/')
def index():
    return jsonify(json.dumps({'Status': 'OK'}))

# it's called by grafana webhook to notify alert
@app.route('/notify', methods=['POST'])
def notify():
    try:
        jsonRep = request.get_json()
        if jsonRep is None:
            raise ValueError('notify request cannot be parsed as json')
        text = jsonRep['title'] + '\nMessage: ' + jsonRep['message']
        if jsonRep['state'] == 'alerting':
            text += '\n' + str(jsonRep["evalMatches"][0]["value"])
        alert(text)
    except Exception as err:
        app.logger.error(err.args)
    else:
        return jsonify(json.dumps({'Status': 'OK'}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
