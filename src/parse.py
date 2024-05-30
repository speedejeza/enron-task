from abc import ABC, abstractmethod
from ctypes import Union
import re
from rich import print
from importlib.resources import files
from symspellpy import SymSpell, Verbosity


class Parse(ABC):
    @abstractmethod
    def parse_search_text(self, search_text: str) -> str:
        """
        Parses the search text and returns a modified version of the text.

        Args:
            search_text (str): The search text to be parsed.

        Returns:
            str: The modified version of the search text.

        """
        pass


class MySQLParse(Parse):
    """
    A class for parsing search text into a MySQL-ready search string for Boolean mode.
    """

    def __init__(self, mode: str) -> None:
        if mode not in ["boolean", "natural"]:
            raise ValueError("Invalid mode. Choose either 'boolean' or 'natural'.")
        self.mode = mode

        # Ref: https://symspellpy.readthedocs.io/en/latest/examples/lookup_compound.html
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        pkg_resource_path = files("symspellpy")
        dictionary_path = str(pkg_resource_path / "frequency_dictionary_en_82_765.txt")
        self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

    def parse_search_text(self, search_text: str) -> str:
        if self.mode == "boolean":
            return self._parse_boolean_mode(search_text)
        elif self.mode == "natural":
            return self._parse_natural_mode(search_text)
        else:  # Should never reach here
            return search_text

    def _parse_boolean_mode(self, search_text: str) -> str:
        # Split the search text into tokens
        tokens = re.split(r'(\s|"|\(|\))', search_text)

        del_space = False
        for i, token in enumerate(tokens):
            # Special/Logic words
            if token == "AND":
                tokens[i] = "+"
                del_space = not del_space
                continue
            elif token == "OR":
                tokens[i] = ""
                del_space = not del_space
                continue
            elif token == " " and del_space:
                tokens[i] = ""
                del_space = not del_space
                continue
            elif token in ['"', "(", ")", " ", ""]:
                continue

            suggestions = self.sym_spell.lookup(
                token, Verbosity.CLOSEST, max_edit_distance=2
            )

            # if suggestions is empty, use the original token
            tokens[i] = suggestions[0].term if suggestions else token

        return "".join(tokens)

    def _parse_natural_mode(self, search_text: str) -> str:
        # Only perform autocorrect on the search text
        suggestions = self.sym_spell.lookup_compound(search_text, max_edit_distance=2)
        return suggestions[0].term if suggestions else search_text


if __name__ == "__main__":
    # Example usage
    parse = MySQLParse(mode="boolean")
    search_text = '"enrgy tradin" bankruptcy AND (lay OR skilling)'
    parsed_text = parse.parse_search_text(search_text)
    print(parsed_text)
