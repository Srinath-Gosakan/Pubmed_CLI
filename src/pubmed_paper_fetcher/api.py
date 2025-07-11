import requests
import xml.etree.ElementTree as ET
from typing import List, Dict


def fetch_pubmed_ids(query: str, retmax: int = 50) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]


def fetch_pubmed_metadata(pubmed_ids: List[str]) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    articles = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or "N/A"
        title = article.findtext(".//ArticleTitle") or "N/A"
        pub_date_elem = article.find(".//PubDate")
        year = pub_date_elem.findtext("Year") if pub_date_elem is not None else "N/A"
        month = pub_date_elem.findtext("Month") or "01"
        day = pub_date_elem.findtext("Day") or "01"
        publication_date = f"{year}-{month}-{day}"

        authors = []
        for author_elem in article.findall(".//Author"):
            name = " ".join(filter(None, [
                author_elem.findtext("ForeName"),
                author_elem.findtext("LastName")
            ])) or "Unknown"
            aff = author_elem.findtext(".//AffiliationInfo/Affiliation") or ""
            email = None
            if "@" in aff:
                words = aff.split()
                for word in words:
                    if "@" in word:
                        email = word.strip(".,;()")
                        break
            authors.append({"name": name, "affiliation": aff, "email": email})

        articles.append({
            "pubmed_id": pmid,
            "title": title,
            "publication_date": publication_date,
            "authors": authors
        })

    return articles
