from src.app import app
from src.queries import get_art_painting_by_code
from src.utils import api_resource_response, api_error_response
from src.constansts import *


@app.route('/')
def hello_world():
    return 'Hello to RecoArt API'


@app.route(BASE_URI_V1 + URI_RECOART_PAINT + RECOART_CODE_PARAM, methods=[GET])
def get_art_painitings_by_code(recoart_code):
    code, recoart_paint = get_art_painting_by_code(recoart_code)
    if code is OK:
        return api_resource_response(recoart_paint, code)
    else:
        return api_error_response(code)
