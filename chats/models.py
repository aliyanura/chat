from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')        
    user_two = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'chats'
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')        
    message = models.CharField(max_length=350, verbose_name='Сообщение')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message
    
    class Meta:
        db_table = 'messages'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('created_at',)
