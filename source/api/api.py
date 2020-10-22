from core import app, config
from flask import request
import json
from base64 import decodebytes
from source.handler.handler import Handler
from io import BytesIO


@app.route('/w2j/run', methods=['POST'])
def on_run():
    try:
        data = json.loads(request.data)
    except:
        return 'Invalid json', 400

    if config['key']:
        if not data.get('key') or data.get('key') != config['key']:
            return 'Invalid key', 400

    if not data.get('image'):
        return 'Empty image passed', 400

    try:
        image = BytesIO(decodebytes(data['image'].encode()))
    except:
        return 'Invalid base64 passed'

    try:
        return Handler(image).run(), 200
    except Exception as e:
        return e, 500


