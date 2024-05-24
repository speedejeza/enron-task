# Enron Task for Energetica
A command-line app with a single argument: `<search-text>` that outputs results as text.
Searches through Enron's email data with the purpose of finding relevant (incriminating) information.

Data source: http://www.ahschulz.de/enron-email-data/

## Setup 

### Requirements
- Docker
- Python >=3.10

### Steps

**Start MySQL Docker Container**
```zsh
docker compose up -d
docker exec -i $CONTAINER_NAME sh -c 'exec mysql -u user -p"password" enron' < ./data/enron-mysqldum_v5.sql
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```zsh
python3 main.py <search-text>
```

`<search-text>`: A string containing a list of keywords to search for. The keywords can include misspellings and other artifacts, and can be specified in any order.