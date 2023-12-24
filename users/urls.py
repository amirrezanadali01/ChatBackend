from django.contrib import admin
from django.urls import path
from users.views import TotalUserApi

urlpatterns = [
    path('total/', TotalUserApi.as_view() , name='total_user'),
]
