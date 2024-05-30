# Energetica Enron Search

Energetica Enron Search is a command-line application that allows you to search through the Enron email dataset for relevant information. The primary purpose of this tool is to assist in finding potentially incriminating evidence from the infamous Enron scandal.

## Getting Started

### Prerequisites

- Docker
- Python 3.10 or later

### Installation

1. Clone the repository:

```bash
git clone https://github.com/speedejeza/enron-task.git
cd enron-task
```

2. Download the SQL dump file from http://www.ahschulz.de/enron-email-data/ and place it in the `/data` folder.

3. Create a `.env` file in the project root directory and provide the required environment variables. You can use the following example as a reference:

```toml
# Shared Environment Variables
DATABASE="enron"
USER="user"
PASSWORD="password"
DATA_PATH="./data/enron-mysqldum_v5.sql"

# Python Environment Variables
HOST="localhost"

# Docker/MySQL Environment Variables
ROOT_PASSWORD="root"
CONTAINER_NAME="enron_db"
```

4. Start the MySQL Docker container:

```bash
docker compose up -d
```

This will take a few minutes to restore the SQL dump file.

5. Set up the virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 setup.py develop
```

### Usage

To search the Enron email dataset, run the following command:

```bash
python3 main.py <search-text>
```

Replace `<search-text>` with a string containing a list of keywords to search for. The keywords can include misspellings and other artifacts, and can be specified in any order.

Example
```bash
python3 main.py 'skilling'
python3 main.py '"enrgy tradin" bankruptcy AND (lay OR skilling)'
```

### Testing

To run the tests, execute the following command:

```bash
pytest tests/test_parse.py
```