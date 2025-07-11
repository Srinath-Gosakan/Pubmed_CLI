import typer
from rich import print
from .api import fetch_pubmed_ids, fetch_pubmed_metadata
from .models import Paper, Author
from .filters import get_non_academic_authors, extract_company_names
from typing import Optional
from .csv_writer import save_to_csv

app = typer.Typer()


@app.command()
def main(
    query: str,
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
):
    if debug:
        print(f"[bold blue]Querying PubMed for:[/bold blue] {query}")

    ids = fetch_pubmed_ids(query)
    if debug:
        print(f"[green]Fetched {len(ids)} paper IDs[/green]")

    metadata = fetch_pubmed_metadata(ids)
    papers = []

    for entry in metadata:
        authors = [Author(**a) for a in entry["authors"]]
        non_academic_authors = get_non_academic_authors(authors)
        if not non_academic_authors:
            continue

        companies = extract_company_names(non_academic_authors)
        corresponding_email = next((a.email for a in authors if a.email), None)

        paper = Paper(
            pubmed_id=entry["pubmed_id"],
            title=entry["title"],
            publication_date=entry["publication_date"],
            non_academic_authors=non_academic_authors,
            companies=companies,
            corresponding_email=corresponding_email
        )
        papers.append(paper)

    if not papers:
        print("[yellow]No papers found with non-academic authors.[/yellow]")
        raise typer.Exit()

    if file:
        save_to_csv(papers, file)
        print(f"[green]Saved {len(papers)} papers to [bold]{file}[/bold][/green]")
    else:
        for paper in papers:
            print(f"[bold]{paper.title}[/bold] ({paper.pubmed_id})")
            print(f"  📅 {paper.publication_date}")
            print(f"  🧑‍🔬 Authors: {', '.join(a.name for a in paper.non_academic_authors)}")
            print(f"  🏢 Companies: {', '.join(paper.companies)}")
            print(f"  ✉️ Email: {paper.corresponding_email or 'N/A'}\n")


if __name__ == "__main__":
    app()
