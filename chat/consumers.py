import json

from channels.generic.websocket import WebsocketConsumer
from chat.models import Room, Actor
from chat.chat import save_message, get_completion


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.lanugage = self.scope["url_route"]["kwargs"]["language"]
        self.room, created = Room.objects.get_or_create(
            owner=self.user, language=self.lanugage
        )
        self.accept()
        self.send_initial_messages(created)

    def send_initial_messages(self, created):
        if created:
            message = save_message(
                self.room, Actor.ASSISTANT, get_completion(self.lanugage)
            )
            self.send(text_data=json.dumps({"actor": "assistant", "message": message}))
        else:
            history = self.room.messages.order_by("timestamp").values(
                "actor", "content"
            )
            for message in history:
                self.send(
                    text_data=json.dumps(
                        {"actor": message["actor"], "message": message["content"]}
                    )
                )

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        reply = save_message(self.room, Actor.USER, message)

        self.send(text_data=json.dumps({"actor": "assistant", "message": reply}))
