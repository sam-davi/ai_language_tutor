import json

from channels.generic.websocket import WebsocketConsumer
from chat.models import Room, Actor
from chat.chat import save_message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.lanugage = self.scope["url_route"]["kwargs"]["language"]
        self.room = Room.objects.get(owner=self.user, language=self.lanugage)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        reply = save_message(self.room, Actor.USER, message)

        self.send(text_data=json.dumps({"message": reply}))
