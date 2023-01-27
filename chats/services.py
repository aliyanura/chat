from django.db.models import Q
from chats.models import Message
from users.services import UserService


class MessageService:
    model = Message

    @classmethod
    def filter(cls, user, companion_pk):
        companion = UserService.get(id=companion_pk)
        return cls.model.objects.filter(
            Q(sender=user)|
            Q(receiver=user),
            Q(sender=companion)|
            Q(receiver=companion),
        )
