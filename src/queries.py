from src.models import Paint, Description
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict
from src.constansts import OK, NOT_FOUND, SERVER_ERROR
from src.wikidata_api import get_wikidata_descriptions
from src.dtos import DescriptionWikidataDTO


def get_art_painting_by_code(code):
    try:
        recoart_paint = Paint.select().where(Paint.Code == code).get()
        if recoart_paint.ExistWikiDescription:
            language_descriptions = ''
            recoart_descriptions = []
            for description in recoart_paint.Descriptions:
                language_descriptions += str(description.Language) + ','
                recoart_descriptions.append(description)
            language_descriptions = language_descriptions[:-1]
            wikidata_code, wikidata_descriptions_response = get_wikidata_descriptions(recoart_paint.Code,
                                                                                      language_descriptions)
            if wikidata_code is OK:
                wikidata_descriptions = wikidata_descriptions_response.Descriptions
                recoart_paint_descriptions = []
                for wikidata_description in wikidata_descriptions:
                    recoart_paint_descriptions \
                        .append(
                        create_recoart_paint_wikidata_description(recoart_descriptions,
                                                                  wikidata_description))
                recoart_paint.Descriptions = recoart_paint_descriptions
    except DoesNotExist:
        return NOT_FOUND, ''
    except:
        return SERVER_ERROR, ''
    return OK, model_to_dict(recoart_paint, backrefs=True)


def create_recoart_paint_wikidata_description(recoart_paint_descriptions: [], wikidata_description: list ) -> Description:
    wikidata_description = DescriptionWikidataDTO(**wikidata_description)
    for recoart_description in recoart_paint_descriptions:
        if recoart_description.Language is wikidata_description.Language:
            recoart_description.Description = wikidata_description.Description
            return recoart_description
