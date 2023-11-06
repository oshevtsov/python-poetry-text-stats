import pytest

from text_stats.stats import count_characters, count_lines, count_words


@pytest.fixture
def input_special_symbols():
    return "$@&+-\n\n\t;:, "


@pytest.fixture
def input_one_word():
    return "abcd_123"


@pytest.fixture
def input_multiline():
    return "Hi, how are you?\nI am good, and you?"


# -----------------------------
# Test count_characters
# -----------------------------
def test_count_characters_empty_string():
    assert count_characters("") == 0


def test_count_characters_one_word(input_one_word: str):
    assert count_characters(input_one_word) == 8


def test_count_characters_special_symbols(input_special_symbols: str):
    assert count_characters(input_special_symbols) == 12


def test_count_characters_multiline(input_multiline: str):
    assert count_characters(input_multiline) == 36


# -----------------------------
# Test count_words
# -----------------------------
def test_count_words_empty_string():
    assert count_words("") == 0


def test_count_words_one_word(input_one_word: str):
    assert count_words(input_one_word) == 1


def test_count_words_special_symbols(input_special_symbols: str):
    assert count_words(input_special_symbols) == 0


def test_count_words_multiline(input_multiline: str):
    assert count_words(input_multiline) == 9


# -----------------------------
# Test count_lines
# -----------------------------
def test_count_lines_empty_string():
    assert count_lines("") == 0


def test_count_lines_one_word(input_one_word: str):
    assert count_lines(input_one_word) == 1


def test_count_lines_special_symbols(input_special_symbols: str):
    assert count_lines(input_special_symbols) == 3


def test_count_lines_multiline(input_multiline: str):
    assert count_lines(input_multiline) == 2
