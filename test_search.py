import pytest

# Test data
search_texts = [
    "enron scandal",
    '"energy trading" OR "california crisis"',
    "bankruptcy AND (lay OR skilling)",
    "shreadding confidential",
    '"special purpose entities" AND "off-balance-sheet"',
    '"jeff skilling" "kenneth lay"',
    '"kenneth lay" Houston',
    '"andrew fastow" accounting tricks',
    'raptors AND "LJM" AND "off-books"',
    '"code of ethics" violation',
    "(enron OR california) AND blackout",
    '(california OR "west coast") AND (energy AND crisis)',
    '"mark to market" accounting',
    '"arthur andersen" AND shredding',
    '"bank of america" AND "merrill lynch"',
    '"congressional hearings" testimony',
    '"stock options" AND "executive compensation"',
    '"natural gas" AND "price manipulation"',
    '"insider trading" AND (lay OR skilling)',
]


# Mock search function
def mock_search(search_text):
    # Implement search logic here
    # For testing purposes, return a dummy list of email IDs
    return [f"email_{i}" for i in range(5)]


@pytest.mark.parametrize("search_text", search_texts)
def test_search(search_text):
    # Call the search function with the test case
    results = mock_search(search_text)

    # Assert that the search function returns a non-empty list of email IDs
    assert isinstance(results, list)
    assert len(results) > 0
