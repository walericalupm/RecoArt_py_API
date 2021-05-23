from src.api import *
from src.app import load_database, app
from src.constants import PORT, DEFAULT_APP_PORT, DEFAULT_APP_HOST


if __name__ == '__main__':
    load_database()
    app.debug = True
    app.run(port=int(os.environ.get(PORT, DEFAULT_APP_PORT)),
            debug=False,
            host=DEFAULT_APP_HOST)

