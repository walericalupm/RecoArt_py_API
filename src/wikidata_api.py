import requests
from src.constants import RECOART_WIKI_DESCRIPTIONS_URI, OK, RECOART_WIKI_DESCRIPTIONS_LANGUAGE_PARAM
from src.dtos import DescriptionsWikidataDTO


def get_wikidata_descriptions(recoart_paint_code: str, language: str) -> DescriptionsWikidataDTO:
    recoart_wiki_request_url = RECOART_WIKI_DESCRIPTIONS_URI + recoart_paint_code \
                               + '?' + RECOART_WIKI_DESCRIPTIONS_LANGUAGE_PARAM + '=' + language
    recoart_wiki_api_response = requests.get(recoart_wiki_request_url)
    if recoart_wiki_api_response.status_code is OK:
        wiki_descriptions_json = recoart_wiki_api_response.json()
        wiki_descriptions = DescriptionsWikidataDTO(**wiki_descriptions_json)
        return OK, wiki_descriptions
    return recoart_wiki_api_response.status_code, None



