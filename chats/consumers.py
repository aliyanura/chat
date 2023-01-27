from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
import json
from chats.models import Message, Chat


class ChatConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    async def connect(self):
        self.chat_pk = self.scope['url_route']['kwargs']['chat_pk']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


        chat = Chat.objects.get(pk=self.chat_pk)
        msg = Message.objects.create(sender=self.scope["user"], message=message, chat=chat)


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope["user"].username
            }
        )


    async def chat_message(self, event):
        message = event['message']
        username = event['username']


        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
