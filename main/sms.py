from flask import current_app, request, jsonify, json
from . import main_blueprint
from .sms_util import alert
import traceback

@main_blueprint.route('/')
def index():
    return jsonify(json.dumps({'Status': 'OK'}))

@main_blueprint.route('/notify', methods=['POST'])
def notify():
    try:
        #current_app.logger.info(request.url)
        jsonRep = request.get_json()
        if jsonRep is not None:
            text = jsonRep['title'] + '\nMessage: ' + jsonRep['message']
            if jsonRep['state'] == 'alerting':
                text += '\n' + str(jsonRep["evalMatches"][0]["value"])
        #current_app.logger.info(text)
        alert(text)
    except Exception:
        current_app.logger.error(traceback.print_exc())
    else:
        return jsonify(json.dumps({'Status': 'OK'}))
