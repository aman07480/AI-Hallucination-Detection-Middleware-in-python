from django.urls import path
from .views import fake_ai_response

urlpatterns = [

    path("ai/chat/", fake_ai_response),

]