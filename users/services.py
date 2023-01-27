from typing import Tuple
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.exceptions import ObjectNotFoundException


class TokenService:
    model = Token

    @classmethod
    def create_auth_token(cls, username: str, password: str) -> Tuple[User, Token]:
        user = authenticate(username=username, password=password)
        if user:
            token, created = cls.model.objects.get_or_create(user=user)
            return user, token
        else:
            raise ObjectNotFoundException('User not found or not active')


class UserService:
    model = User

    @classmethod
    def get(cls, *args, **kwargs) -> model:
        try:
            return cls.model.objects.get(**kwargs)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException(f'{cls.model.__name__} not found')
