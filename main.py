import mysql.connector
import config


def main():
    mydb = mysql.connector.connect(**config.db)

    print(mydb)


if __name__ == "__main__":
    main()
