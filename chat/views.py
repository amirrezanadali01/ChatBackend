from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ChatSeralizers
from .models import ChatModel
# Create your views here.

class GetTotalChats(ListAPIView):
    serializer_class = ChatSeralizers
    def get_queryset(self):
        chats = ChatModel.objects.filter(receiver= self.kwargs['receiver'] , sender= self.request.user.id )
        print(self.request.user)
        return chats


    