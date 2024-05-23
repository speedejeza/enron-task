import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    "host": os.getenv("HOST"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("DATABASE"),
}

def main():
    mydb = mysql.connector.connect(**db_config)

    print(mydb)


if __name__ == "__main__":
    main()
