import unittest
from faker import Faker
from random import randint, seed
from dotenv import dotenv_values
from src.constansts import ENV_TEST_DIR
import src.models as models
from src.constansts import

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_database()
        drop_tables()
        create_tables()
        seed_database()

    @classmethod
    def tearDownClass(cls):
        drop_tables()


recoart_paints = []


def load_database():
    db_params = dotenv_values(ENV_TEST_DIR)
    models.remote_db.init(
        db_params.get('DATABASE_NAME'),
        user=db_params.get('DATABASE_USERNAME'),
        password=db_params.get('DATABASE_PASSWORD'),
        host=db_params.get('DATABASE_HOST'),
        port=int(db_params.get('DATABASE_PORT'))
    )


def create_tables():
    with models.remote_db as db:
        db.create_tables([models.Paint, models.Description])


def drop_tables():
    with models.remote_db as db:
        db.drop_tables([models.Paint, models.Description])


def seed_database():
    


def get_random_wikipedia_paint_catalog() -> models.WikipediaPaintCatalog:
    wikipedia_catalog_paints_lenght = len(wikipedia_catalog_paints) - 1
    random_position = randint(0, wikipedia_catalog_paints_lenght)
    return wikipedia_catalog_paints[random_position]


def get_recoart_fake_code() -> str:
    fake = Faker()
    seed(0)
    return fake.bothify(text='AP_99#_###')


def get_wikidata_random_language() -> str:
    random_language_int = randint(0, 3)
    if random_language_int == 0:
        return LANG_ES
    if random_language_int == 1:
        return LANG_EN
    if random_language_int == 2:
        return LANG_FR
    else: return LANG_IT
