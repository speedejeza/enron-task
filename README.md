# Enron Task for Energetica
A command-line app with a single argument: `<search-text>` that outputs results as text.
Searches through Enron's email data with the purpose of finding relevant (incriminating) information.


## Setup 

### Requirements
- Docker
- Python >=3.10


### Download SQL Dump file
1. Download http://www.ahschulz.de/enron-email-data/
2. Place in `/data` folder


### Start MySQL Docker Container
```zsh
docker compose up -d
```
This will take a few minutes for MySQL to restore the SQL Dump file.


### Setup Virtual Environment
```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```zsh
python3 main.py <search-text>
```

`<search-text>`: A string containing a list of keywords to search for. The keywords can include misspellings and other artifacts, and can be specified in any order.