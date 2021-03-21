from app import app
from flask import jsonify, request
from playhouse.shortcuts import model_to_dict
from queries import get_art_paintings_by_code


@app.route('/api/art/code/<code>')
def get_art_painitings_by_code(code):
    # withimg = request.args['withimg']
    # lan = request.args['lan']
    paint = get_art_paintings_by_code(code)
    return jsonify(model_to_dict(paint, backrefs=True))
