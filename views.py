from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def fake_ai_response(request):

    prompt = request.data.get("prompt")

    ai_response = """
    I think this answer is probably correct,
    but I am not sure.
    """

    return Response({
        "prompt": prompt,
        "response": ai_response
    })