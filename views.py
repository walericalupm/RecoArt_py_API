from app import app
from flask import jsonify
from playhouse.shortcuts import model_to_dict
from queries import get_art_paintings_by_code


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/art/code/<code>')
def get_art_painitings_by_code(code):
    paint = get_art_paintings_by_code(code)
    return jsonify(model_to_dict(paint, backrefs=True))