import re


def clean_text(text):
    text = re.sub(r"[^가-힣a-zA-Z0-9\s]", "", text)
    return text.strip()
