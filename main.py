from src.api import *
from src.app import load_database, app


if __name__ == '__main__':
    load_database()
    app.debug = True
    app.run(port=int(os.environ.get("PORT", 80)),
            debug=True,
            host='0.0.0.0')

