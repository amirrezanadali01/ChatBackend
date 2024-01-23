from django.urls import path
from .consumers import WSChat
ws_urlpatterns = [
  path('ws/chat/<str:access>/<int:user>/', WSChat.as_asgi())
]