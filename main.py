import os
from dotenv import load_dotenv
from fire import Fire
from src.search import MySQLSearch


def main(search_text: str, limit: int = 10):
    load_dotenv()

    db_config = {
        "host": os.getenv("HOST"),
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "database": os.getenv("DATABASE"),
    }

    searchobj = MySQLSearch(**db_config)
    results = searchobj.search(search_text, limit)
    print(results)


if __name__ == "__main__":
    Fire(main)
