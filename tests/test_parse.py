import pytest

from src.parse import MySQLParse


@pytest.fixture
def parser() -> MySQLParse:
    return MySQLParse(mode="boolean")


class TestParse:
    def test_parse_search_text_phrases(self, parser):
        search_text = '"energy trading" OR "california crisis"'
        expected_sql_string = '"energy trading" "california crisis"'
        assert parser.parse_search_text(search_text) == expected_sql_string

    def test_parse_search_text_logical_operators(self, parser):
        search_text = "bankruptcy AND (lay OR skilling)"
        expected_sql_string = "bankruptcy +(lay skilling)"
        assert parser.parse_search_text(search_text) == expected_sql_string

    def test_parse_search_text_mixed(self, parser):
        search_text = '"kenneth lay" "energy trading" AND crisis'
        expected_sql_string = '"kenneth lay" "energy trading" +crisis'
        assert parser.parse_search_text(search_text) == expected_sql_string

    def test_parse_search_text_empty(self, parser):
        search_text = ""
        expected_sql_string = ""
        assert parser.parse_search_text(search_text) == expected_sql_string

    def test_parse_search_text_no_phrases(self, parser):
        search_text = "bankruptcy lay skilling"
        expected_sql_string = "bankruptcy lay skilling"
        assert parser.parse_search_text(search_text) == expected_sql_string

    def test_parse_search_text_spelling_error(self, parser):
        search_text = '"enrgy tradin" bankruptcy AND (lay OR skilling)'
        expected_sql_string = '"energy trading" bankruptcy +(lay skilling)'
        assert parser.parse_search_text(search_text) == expected_sql_string
