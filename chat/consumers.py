from channels.generic.websocket import WebsocketConsumer , AsyncWebsocketConsumer
import json
from time import sleep
from chat.models import ChatModel
from django.contrib.auth.models import User

from asgiref.sync import sync_to_async
# ws://localhost:8000/ws/counter/
class WSChat(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()
    print('connectttttttttttttttttttttttttttttttt')


  async def disconnect(self, code):
    print('disconnect')
    print(self.scope['user'])

  
  async def receive(self, text_data):
        print('dsjdskjljkfdsjkfjkjkdsfjkdjk')

        text_data_json = json.loads(text_data)
        print(text_data_json)

        await self.save_chat_message(sender= self.scope['user']  ,text=text_data_json['text'] ,receiver=text_data_json['receiver'])

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
  