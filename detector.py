import re

SUSPICIOUS_WORDS = [
    "maybe",
    "probably",
    "i think",
    "not sure",
    "possibly",
    "unknown",
]

def detect_hallucination(text):

    text = text.lower()

    score = 0
    matched_patterns = []

    for word in SUSPICIOUS_WORDS:

        if word in text:
            score += 1
            matched_patterns.append(word)

    hallucination_detected = score >= 2

    return {
        "hallucination": hallucination_detected,
        "score": score,
        "matched_patterns": matched_patterns
    }