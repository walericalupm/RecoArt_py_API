from flask import render_template, redirect, url_for
from flask_cors import cross_origin
from src.app import app
from src.queries import get_art_painting_by_code
from src.utils import api_resource_response, api_error_response
from src.constansts import *


@app.route(URI_INDEX)
def index():
    return redirect(url_for(GET_API_DOCS_METHOD_NAME))


@app.route(BASE_URI_V1 + URI_API_DOCS)
def get_api_docs():
    return render_template(SWAGGER_TEMPLATE)


@app.route(BASE_URI_V1 + URI_RECOART_PAINT + RECOART_CODE_PARAM, methods=[GET])
@cross_origin()
def get_art_painitings_by_code(recoart_code):
    code, recoart_paint = get_art_painting_by_code(recoart_code)
    if code is OK:
        return api_resource_response(recoart_paint, code)
    else:
        return api_error_response(code)
