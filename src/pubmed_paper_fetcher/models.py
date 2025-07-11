from pydantic import BaseModel
from typing import Optional, List


class Author(BaseModel):
    name: str
    affiliation: Optional[str]
    email: Optional[str]


class Paper(BaseModel):
    pubmed_id: str
    title: str
    publication_date: str
    non_academic_authors: List[Author]
    companies: List[str]
    corresponding_email: Optional[str]
