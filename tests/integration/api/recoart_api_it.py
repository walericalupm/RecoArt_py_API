from tests.base_test_setup import BaseTestCase, get_monalisa_paint
import src.models as models
from src.api import get_art_painitings_by_code
from src.app import app
from src.constansts import OK, BASE_URI_V1, URI_RECOART_PAINT, RECOART_CODE_PARAM


class RecoArtDBIT(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

    def test_get_paint_with_wiki_descriptions(self):
        with app.test_client() as client:
            monalisa_paint_code = get_monalisa_paint().Code
            get_paint_url = BASE_URI_V1 + URI_RECOART_PAINT + '/' + monalisa_paint_code
            response = client.get(get_paint_url)
            wikipedia_descriptions_json = response.get_json()

            self.assertEqual(OK, response.status_code)
            self.assertEqual(4, len(wikipedia_descriptions_json['Descriptions']))
            self.assertEqual(0, wikipedia_descriptions_json['Descriptions'][0]['Language'])
            self.assertEqual(1, wikipedia_descriptions_json['Descriptions'][1]['Language'])
            self.assertEqual(2, wikipedia_descriptions_json['Descriptions'][2]['Language'])
            self.assertEqual(3, wikipedia_descriptions_json['Descriptions'][3]['Language'])

