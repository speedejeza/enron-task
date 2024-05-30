from abc import ABC, abstractmethod
import mysql.connector


class Search(ABC):
    @abstractmethod
    def search(self, text: str, limit: int = 10):
        """
        Search for emails in Enron dataset that match the given text.

        Args:
            text (str): The text to search for.
            limit (int, optional): The maximum number of results to return. Defaults to 10.

        Returns:
            list: A list of messages that match the search query.
        """
        pass


class MySQLSearch(Search):
    def __init__(
        self,
        host: str | None,
        user: str | None,
        password: str | None,
        database: str | None,
    ):
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )
        self.cursor = self.cnx.cursor(prepared=True)

    def search(self, text: str, limit: int = 10):
        stmt = "SELECT * FROM message WHERE MATCH (subject,body) AGAINST (%s IN NATURAL LANGUAGE MODE);"
        self.cursor.execute(stmt, (text,))
        return self.cursor.fetchmany(limit)
