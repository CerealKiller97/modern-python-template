import pytest

from src.util.text import slugify, truncate


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World", "hello-world"),
        ("  Leading and trailing  ", "leading-and-trailing"),
        ("Multiple---dashes", "multiple-dashes"),
        ("Special!@# Chars", "special-chars"),
    ],
)
def test_slugify(text: str, expected: str) -> None:
    assert slugify(text) == expected


def test_truncate_shorter_than_length_returns_unchanged() -> None:
    assert truncate("hello", 10) == "hello"


def test_truncate_longer_than_length_adds_suffix() -> None:
    assert truncate("hello world", 5) == "hello..."


def test_truncate_custom_suffix() -> None:
    assert truncate("hello world", 5, suffix="!") == "hello!"
