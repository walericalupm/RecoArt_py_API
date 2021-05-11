from pydantic import BaseModel
from typing import List


class DescriptionWikidataDTO(BaseModel):
    Language: int
    Name: str
    Pseudonym: str
    Medium: str
    Description: str


class DescriptionsWikidataDTO(BaseModel):
    RecoArtPaintCode: str
    WikipediaPaintCode: str
    Descriptions: List[DescriptionWikidataDTO]






