from rest_framework.serializers import ModelSerializer
from .models import ChatModel

class ChatSeralizers(ModelSerializer):
    class Meta:
        model = ChatModel
        fields = '__all__'