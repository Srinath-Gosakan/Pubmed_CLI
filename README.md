# PubMed Paper Fetcher CLI

A command-line tool to fetch research papers from PubMed based on a query and extract those with at least one non-academic author affiliated with a pharmaceutical or biotech company. Outputs the results as a clean CSV.

---

## Features

- 🔍 Fetch papers using full PubMed query syntax
- 🧑‍🔬 Filter authors affiliated with **non-academic** institutions
- 🏢 Identify **pharma/biotech company** affiliations
- ✉️ Extract **corresponding author email**
- 📦 Poetry-powered and CLI-ready via `get-papers-list`

---

## Output CSV Format

| Column                       | Description                                               |
|------------------------------|-----------------------------------------------------------|
| `PubmedID`                   | Unique PubMed identifier                                  |
| `Title`                      | Paper title                                               |
| `Publication Date`           | Date of publication (YYYY-MM-DD)                          |
| `Non-academic Author(s)`     | Authors not affiliated with universities/institutes       |
| `Company Affiliation(s)`     | Inferred company names from author affiliations           |
| `Corresponding Author Email` | Extracted email if available                              |

---

## Usage

```bash
poetry run get-papers-list "your query here" --file output.csv --debug
```
---

## Options

| Flag                         | Description                                               |
|------------------------------|-----------------------------------------------------------|
| `--file or -f`               | Save results to CSV (default: print to console)           |
| `--debug or -d`              | Show debug output during execution                        |
| `--help or -h`               | Show usage instructions                                   |

---

## Example

```bash
poetry run get-papers-list "cancer immunotherapy" --file results.csv --debug
```
## Output

```bash
Querying PubMed for: cancer immunotherapy
Fetched 50 paper IDs
Saved 12 papers to results.csv
```
---

## Project Structure

```rust
pubmed_paper_fetcher/
├── pyproject.toml         ← Poetry config
├── README.md              ← You're reading this
├── src/
│   └── pubmed_paper_fetcher/
│       ├── api.py         ← PubMed API integration
│       ├── cli.py         ← Typer-based CLI interface
│       ├── csv_writer.py  ← Writes final CSV output
│       ├── filters.py     ← Heuristics to filter company authors
│       └── models.py      ← Pydantic models for Paper/Author
```

---

## Installation

```bash
git clone https://github.com/yourusername/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install
```

---

## Tools and Libraries

1)PubMed E-Utilities API

2)Poetry for packaging & dependency management

3)Typer for CLI

4)Pydantic for typed data models

5)Rich for clean console output

---



