from src.models import Paint
from peewee import DoesNotExist
from src.constansts import OK, NOT_FOUND, SERVER_ERROR
from src.wikidata_api import get_wikidata_descriptions


def get_art_painting_by_code(code):
    try:
        recoart_paint = Paint.select().where(Paint.Code == code).get()
        if recoart_paint.ExistsWikiDescription:
            wikidata_descriptions = get_wikidata_descriptions(recoart_paint.Code).Descriptions

    except DoesNotExist:
        return NOT_FOUND, ''
    except:
        return SERVER_ERROR, ''

    return (Paint
            .select()
            .where(Paint.Code == code).get())
