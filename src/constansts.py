import os

# ROOT Project Path
CURRENT_DIR = 'src'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(CURRENT_DIR, '')
ENV_TEST_DIR = os.path.join(ROOT_DIR, '.env.test')

# API
V1 = '/v1'
BASE_URI_V1 = '/api' + V1
URI_RECOART_PAINT = '/art/code'
RECOART_CODE_PARAM = '/<string:recoart_code>'

# External APIs
RECOART_WIKI_API_URI = "https://recoart-py-wiki-api.herokuapp.com/api/v1"
RECOART_WIKI_DESCRIPTIONS_URI = RECOART_WIKI_API_URI + "/wikidescriptions/"
RECOART_WIKI_DESCRIPTIONS_LANGUAGE_PARAM = 'lang'

JSON_MIME_TYPE = 'application/json'

NOT_FOUND_MESSAGE = 'Resource Not Found'
SERVER_ERROR_MESSAGE = 'Server Error'

# HTTP Response Codes
CREATED = 201
OK = 200
CONFLICT = 409
NOT_FOUND = 404
SERVER_ERROR = 500

# HTTP Methods
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

# Various
MESSAGE = 'message'