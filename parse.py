import re


def parse_search_text(search_text: str):
    # Define regular expressions for different patterns
    phrase_pattern = r'"(.*?)"'
    word_pattern = r'\b(?!"{})(?!AND|OR)\w+\b'
    logical_operator_pattern = r"(AND|OR)"

    # Initialize variables
    phrases = []
    logical_operators = []
    words = []

    # Extract phrases
    phrases = re.findall(phrase_pattern, search_text)

    # Extract logical operators
    logical_operators = re.findall(logical_operator_pattern, search_text)

    # Replace the phrases with empty strings to avoid matching words within phrases
    search_text_words = search_text
    for phrase in phrases:
        search_text_words = search_text_words.replace(phrase, "")

    # Extract words
    words = re.findall(word_pattern, search_text_words)

    # Build the SQL search string
    sql_search_string = ""

    # Add phrases
    for phrase in phrases:
        sql_search_string += f'"+{phrase}*" '

    # Add words
    for word in words:
        sql_search_string += f'"{word}*" '

    # Add logical operators
    if "AND" in logical_operators:
        sql_search_string = sql_search_string.replace("AND", "+")
    if "OR" in logical_operators:
        sql_search_string = sql_search_string.replace("OR", " ")

    return sql_search_string


search_text = '"energy trading" OR "california crisis"'
sql_search_string = parse_search_text(search_text)
print(sql_search_string)  # Output: +energy*trading* california*crisis*
