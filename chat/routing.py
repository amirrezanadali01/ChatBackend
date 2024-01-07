from django.urls import path
from .consumers import WSChat
ws_urlpatterns = [
  path('ws/chat/', WSChat.as_asgi())
]