
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import viewsets,status

from board.models import Board
from board.serializers import BoardSerializers



class BoardAPIViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializers
    permission_classes = (AllowAny,)

    def create(self, request):
        data = request.data
        board_data = data['data'].split("/")
        board_data.pop(0)
    

        return Response(board_data)
