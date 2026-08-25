import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate(text: str, length: int, suffix: str = "...") -> str:
    if len(text) <= length:
        return text
    return text[:length].rstrip() + suffix
