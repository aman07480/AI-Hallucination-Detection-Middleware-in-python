def calculate_confidence(score):

    confidence = 100 - (score * 20)

    if confidence < 0:
        confidence = 0

    return confidence