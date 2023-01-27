from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from chats.serializers import MessageSerializer
from chats.services import MessageService


class CatalogAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        queryset = MessageService.filter(
            user=request.user,
            companion_pk=kwargs.get('companion_pk')
        )
        serializer = self.serializer_class(queryset, many=True)
        return Response(data={
            'message': 'Chat messages',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)