from src import models
from tests.base_test_setup import BaseTestCase, get_recoart_fake_code, get_monalisa_paint, get_recoart_code


class RecoArtDBIT(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

    def test_get_recoart_paint(self):
        recoart_existing_code = get_recoart_code()
        recoart_paint = models.Paint.select().where(models.Paint.Code == recoart_existing_code).get()

        self.assertIsNotNone(recoart_paint)
        self.assertIsNotNone(recoart_paint.Descriptions)







