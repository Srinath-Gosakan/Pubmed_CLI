from typing import List, Optional
from .models import Author


ACADEMIC_KEYWORDS = [
    "university", "college", "school", "institute", "department", "hospital", "faculty", "lab"
]


def is_non_academic(affiliation: Optional[str]) -> bool:
    if not affiliation:
        return False
    return not any(keyword in affiliation.lower() for keyword in ACADEMIC_KEYWORDS)


def get_non_academic_authors(authors: List[Author]) -> List[Author]:
    return [a for a in authors if is_non_academic(a.affiliation)]


def extract_company_names(authors: List[Author]) -> List[str]:
    companies = set()
    for a in authors:
        if a.affiliation and is_non_academic(a.affiliation):
            companies.add(a.affiliation.split(",")[0].strip())
    return list(companies)
