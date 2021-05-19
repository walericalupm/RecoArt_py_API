from pydantic import BaseModel
from typing import List


class DescriptionWikidataDTO(BaseModel):
    Language: int
    Description: str


class DescriptionsWikidataDTO(BaseModel):
    RecoArtPaintCode: str
    WikipediaPaintCode: str
    Descriptions: list




