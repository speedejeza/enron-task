import os
from fire import Fire
from dotenv import load_dotenv
from rich import print
from src.parse import MySQLParse
from src.search import MySQLSearch


def main(search_text: str, limit: int = 10):
    load_dotenv()

    # Parse Search Text
    if search_text is None or search_text == "":
        print("Please provide a search text.")
        return

    if any(x in search_text for x in ["(", ")", "AND", "OR"]):
        mode = "boolean"
    else: 
        mode = "natural"

    parser = MySQLParse(mode)
    parsed_text = parser.parse_search_text(search_text)

    # Perform Search
    db_config = {
        "host": os.getenv("HOST"),
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "database": os.getenv("DATABASE"),
    }
    searchobj = MySQLSearch(mode, **db_config)
    results = searchobj.search(parsed_text, limit, "table")
    print(results)


if __name__ == "__main__":
    Fire(main)
