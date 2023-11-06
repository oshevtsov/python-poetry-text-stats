import re


def count_characters(input: str) -> int:
    """Count charactes in the input string (including whitespace and punctuation)"""
    return len(input)


def count_words(input: str) -> int:
    """Count words in the input string"""
    words = list(filter(lambda w: len(w) > 0, re.split(r"\W+", input)))
    return len(words)


def count_lines(input: str) -> int:
    """Count lines in the input string"""
    return len(input.splitlines())
