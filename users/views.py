from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from users.services import TokenService
from users.serializers import LoginSerializer

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = TokenService.create_auth_token(
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password')
        )
        return Response(data={
            'message': 'You have successfully logged in',
            'data': {
                'token': str(token),
                'token_type': 'Token',
                'user_id': user.pk
            },
            'status': "OK"
        }, status=status.HTTP_200_OK)
