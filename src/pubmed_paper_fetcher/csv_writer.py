import csv
from .models import Paper
from typing import List


def save_to_csv(papers: List[Paper], filename: str) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "PubmedID", "Title", "Publication Date",
            "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
        ])
        for p in papers:
            writer.writerow([
                p.pubmed_id,
                p.title,
                p.publication_date,
                "; ".join(a.name for a in p.non_academic_authors),
                "; ".join(p.companies),
                p.corresponding_email or ""
            ])
