import unittest
from faker import Faker
from random import randint, seed
from dotenv import dotenv_values
from src.constansts import ENV_TEST_DIR
import src.models as models
from random import randrange


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
recoart_paints_descriptions = []


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
    for _ in range(10):
        recoart_paint_to_save = create_fake_paint()
        recoart_paints.append(recoart_paint_to_save)
        recoart_paint_to_save.save()
        # create 1-4 descriptions per paint
        language = 0
        for _ in range(randrange(3)):
            recoart_paint_description_to_save = create_fake_description(recoart_paint_to_save, language)
            recoart_paints_descriptions.append(recoart_paint_description_to_save)
            recoart_paint_description_to_save.save()
            language = language+1
    # Create Mona Lisa Paint
    monalisa_paint = get_monalisa_paint()
    monalisa_paint.save()
    monalisa_fake_description = create_fake_description(monalisa_paint, 0)
    monalisa_fake_description.save()
    monalisa_fake_description = create_fake_description(monalisa_paint, 1)
    monalisa_fake_description.save()


def get_recoart_fake_code() -> str:
    fake = Faker()
    seed(0)
    return fake.bothify(text='AP_99#_###')


def get_recoart_code() -> str:
    recoart_paints_length = len(recoart_paints)
    random_position = randrange(recoart_paints_length)
    return recoart_paints[random_position].Code


def create_fake_paint() -> models.Paint:
    fake = Faker()
    seed(0)
    faker_image_expression = ''.join([char*400 for char in '?#??#?#??##?#'])
    return models.Paint(Code=fake.bothify('AP_99#_###'),
                        Artist=fake.bothify('ARTIST_##'),
                        Year=fake.year(),
                        Location=fake.city(),
                        Image=fake.bothify(faker_image_expression),
                        Link=fake.url(),
                        ExistsWikiDescription=False)


def get_monalisa_paint() -> models.Paint:
    fake = Faker()
    seed(2)
    faker_image_expression = ''.join([char * 400 for char in '?#??#?#??##?#'])
    return models.Paint(Code='AP_001_001',
                        Artist='Leonardo da Vinci',
                        Year=1530,
                        Location='Musée du Louvre, Paris',
                        Image=fake.bothify(faker_image_expression),
                        Link='https://www.louvre.fr/en/oeuvre-notices/mona-lisa-portrait-lisa-gherardini-wife-francesco-del-giocondo',
                        ExistWikiDescription=True)


def create_fake_description(paint: models.Paint, language:int) -> models.Description:
    fake = Faker()
    seed(3)
    return models.Description(Language=language,
                              Name=fake.text(max_nb_chars=20),
                              Pseudonym=fake.text(max_nb_chars=20),
                              Medium=fake.text(max_nb_chars=20),
                              Description=fake.text(max_nb_chars=200),
                              Paint=paint)

