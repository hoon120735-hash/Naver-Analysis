import re
import time


def clean_text(text):
    text = re.sub(r"[^가-힣a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def wait_short(seconds=1):
    time.sleep(seconds)
