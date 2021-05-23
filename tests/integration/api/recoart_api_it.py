from tests.base_test_setup import BaseTestCase, get_monalisa_paint
import src.models as models
from src.api import get_art_painitings_by_code
from src.app import app
from src.constants import OK, BASE_URI_V1, URI_RECOART_PAINT, URI_INDEX, REDIRECT_FOUND


class RecoArtDBIT(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

    def test_redirect_index_to_api_docs(self):
        with app.test_client() as client:
            response = client.get(URI_INDEX)
            self.assertEqual(REDIRECT_FOUND, response.status_code)


    def test_get_paint(self):
        with app.test_client() as client:
            monalisa_paint_code = get_monalisa_paint().Code
            get_paint_url = BASE_URI_V1 + URI_RECOART_PAINT + '/' + monalisa_paint_code
            response = client.get(get_paint_url)
            self.assertEqual(OK, response.status_code)
