import requests
from src.constansts import RECOART_WIKI_DESCRIPTIONS_URI, OK
from src.dtos import DescriptionsWikidataDTO


def get_wikidata_descriptions(recoart_paint_code) -> DescriptionsWikidataDTO:
    recoart_wiki_api_response = requests.get(RECOART_WIKI_DESCRIPTIONS_URI+recoart_paint_code)
    if recoart_wiki_api_response.status_code is OK:
        wiki_descriptions_json = recoart_wiki_api_response.json()
        wiki_descriptions = DescriptionsWikidataDTO(**wiki_descriptions_json)
        return OK, wiki_descriptions
    return recoart_wiki_api_response.status_code, None



