import pytest
from parse import parse_search_text

def test_parse_search_text_phrases():
    search_text = '"energy trading" OR "california crisis"'
    expected_sql_string = '"energy trading" "california crisis"'
    assert parse_search_text(search_text) == expected_sql_string

def test_parse_search_text_logical_operators():
    search_text = 'bankruptcy AND (lay OR skilling)'
    expected_sql_string = 'bankruptcy +lay +skilling'
    assert parse_search_text(search_text) == expected_sql_string

def test_parse_search_text_mixed():
    search_text = '"kenneth lay" Houston "energy trading" AND crisis'
    expected_sql_string = '+kenneth*lay* Houston* +energy*trading* crisis*'
    assert parse_search_text(search_text) == expected_sql_string

def test_parse_search_text_empty():
    search_text = ''
    expected_sql_string = ''
    assert parse_search_text(search_text) == expected_sql_string

def test_parse_search_text_no_phrases():
    search_text = 'bankruptcy lay skilling'
    expected_sql_string = 'bankruptcy* lay* skilling*'
    assert parse_search_text(search_text) == expected_sql_string