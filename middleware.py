import json

from .detector import detect_hallucination
from .confidence_engine import calculate_confidence
from .suspicious_patterns import regex_pattern_check


class AIHallucinationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)

        try:

            if request.path.startswith("/api/ai/"):

                data = json.loads(response.content)

                ai_text = data.get("response", "")

                detection = detect_hallucination(ai_text)

                regex_matches = regex_pattern_check(ai_text)

                confidence = calculate_confidence(
                    detection["score"]
                )

                data["hallucination_analysis"] = {
                    "detected": detection["hallucination"],
                    "confidence": confidence,
                    "matched_words": detection["matched_patterns"],
                    "regex_matches": regex_matches
                }

                response.content = json.dumps(data)

        except Exception as e:
            print("Middleware Error:", e)

        return response