from channels.generic.websocket import WebsocketConsumer , AsyncWebsocketConsumer
import json
from time import sleep
from chat.models import ChatModel
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer

# ws://localhost:8000/ws/counter/
class WSChat(AsyncWebsocketConsumer):
  async def connect(self):
    
    # Comparison ids
    

    token = self.scope['url_route']['kwargs']['access']
    token = AccessToken(token=token)
    self.scope['user'] = token['user_id']
    self.other_user = self.scope['url_route']['kwargs']['user']
    me = self.scope['user']
    other_user = self.other_user
    

    if(me > other_user):
        group_name = f'{me}_{other_user}'
    else:
        group_name = f'{other_user}_{me}'

    # create group
    self.group_name = f'chat_{group_name}' #my salt is chat


    await self.channel_layer.group_add(
            self.group_name ,
            self.channel_name
        )

    await self.accept()


  async def disconnect(self, code):
    await self.channel_layer.group_discard(
            self.group_name , 
            self.channel_name 
        )

  
  async def receive(self, text_data):
        text_data_json = json.loads(text_data)  

        await self.save_chat_message(sender= self.scope['user']  ,text=text_data_json['text'] ,receiver=self.other_user)

  @sync_to_async
  def save_chat_message(self, sender, text , receiver):
        
        sender = User.objects.get(id = sender)
        receiver = User.objects.get(id = receiver)

        chat_message = ChatModel.objects.create(
            text=text,
            receiver=receiver,
            sender=sender
        )
        



        # send chat message event to the room
  