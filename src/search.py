from abc import ABC, abstractmethod
import mysql.connector
from rich.table import Table


class Search(ABC):
    @abstractmethod
    def search(self, text: str, limit: int = 10, output_format: str = "str"):
        """
        Search for emails in Enron dataset that match the given text.

        Args:
            text (str): The text to search for.
            limit (int, optional): The maximum number of results to return. Defaults to 10.
            output_format (str, optional): The format of the output. Defaults to "str". Options: "str", "table".

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

    def search(self, text: str, limit: int = 10, output_format: str = "str"):
        stmt = "SELECT * FROM message WHERE MATCH (subject,body) AGAINST (%s IN NATURAL LANGUAGE MODE);"
        self.cursor.execute(stmt, (text,))

        if output_format == "str":
            return self.cursor.fetchmany(limit)
        elif output_format == "table":
            return self.__output_table(self.cursor.fetchmany(limit))

    def __output_table(self, results: list):
        table = Table(title="Search Results", padding=(1, 1))

        # Add columns to the table
        colours = ["red", "green", "blue", "yellow", "magenta", "cyan", "bright_black"]
        for i, column in enumerate(self.cursor.column_names):
            table.add_column(column, style=f"{colours[i % len(colours)]}")


        # Add rows to the table
        for result in results:
            str_result = [str(i) for i in result]  # Convert all elements to string
            table.add_row(*str_result)

        return table
