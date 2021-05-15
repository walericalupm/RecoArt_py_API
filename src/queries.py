from src.models import Paint, Description
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict
from src.constansts import OK, NOT_FOUND, SERVER_ERROR
from src.wikidata_api import get_wikidata_descriptions


def get_art_painting_by_code(code):
    try:
        recoart_paint = Paint.select().where(Paint.Code == code).get()
        if recoart_paint.ExistWikiDescription:
            wikidata_code, wikidata_descriptions_response = get_wikidata_descriptions(recoart_paint.Code)
            if wikidata_code is OK:
                wikidata_descriptions = wikidata_descriptions_response.Descriptions
                recoart_paint_descriptions = []
                for wikidata_description in wikidata_descriptions:
                    recoart_paint_descriptions \
                        .append(
                        Description(Language=wikidata_description.Language,
                                    Name=wikidata_description.Name,
                                    Pseudonym=wikidata_description.Pseudonym,
                                    Medium=wikidata_description.Medium,
                                    Description=wikidata_description.Description,
                                    Paint=wikidata_description))
                recoart_paint.Descriptions = recoart_paint_descriptions
    except DoesNotExist:
        return NOT_FOUND, ''
    except:
        return SERVER_ERROR, ''
    return OK, model_to_dict(recoart_paint, backrefs=True)


