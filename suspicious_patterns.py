import re

PATTERNS = [
    r"i am not sure",
    r"cannot verify",
    r"might be incorrect",
]

def regex_pattern_check(text):

    found = []

    for pattern in PATTERNS:

        if re.search(pattern, text.lower()):
            found.append(pattern)

    return found