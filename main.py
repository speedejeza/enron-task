import mysql.connector
import os
from dotenv import load_dotenv
import fire

load_dotenv()

db_config = {
    "host": os.getenv("HOST"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("DATABASE"),
}

def main(search_text: str):
    # Connect to the database
    mydb = mysql.connector.connect(**db_config)
    mycursor = mydb.cursor()
    
    # Search for the text in the database
    mycursor.execute(f"SELECT * FROM books WHERE title LIKE '%{search_text}%'")
    
    print(mydb)


if __name__ == "__main__":
    fire.Fire(main)
