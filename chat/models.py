from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatModel(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete = models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name = 'receiver')
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default = False)