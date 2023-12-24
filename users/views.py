from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User

from users.serializers import TotalUserSeralizer
# Create your views here.

class TotalUserApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = TotalUserSeralizer
