import mysql.connector


def main():
    mydb = mysql.connector.connect(
        host="localhost", user="admin", password="admin"
    )
    
    print(mydb)


if __name__ == "__main__":
    main() 
