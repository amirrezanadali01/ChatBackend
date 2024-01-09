from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep


# ws://localhost:8000/ws/counter/
class WSChat(WebsocketConsumer):
  def connect(self):
    self.accept()
    count = 0
    

    for i in range(1000):
      if count < 10:
        count += 1
        self.send(json.dumps({'message': count}))
        sleep(1)
      else:
        count = 1
        self.send(json.dumps({'message': count}))
        sleep(1)

  def disconnect(self, code):
    print('disconnect')
    print(code)