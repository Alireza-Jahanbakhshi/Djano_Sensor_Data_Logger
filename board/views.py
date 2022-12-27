from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status

from board.models import Board
from board.serializers import BoardSerializers
from board.utils import create_data_format


class BoardAPIViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializers
    permission_classes = (AllowAny,)

    def create(self, request):
        data = request.data
        board_data = data['data'].split("/")
        board_data.pop(0)
        serializer = self.get_serializer(data=create_data_format(board_data))
        if not serializer.is_valid():
            return Response({
                "error": serializer.errors
            }, status=400)

        serializer.save()
        return Response({
            "data": serializer.data
        }, status=200)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj)
        return Response({
            "data": obj.send_data_type
        }, status=200)


def board_view(request):
    return render(request, 'index.html')
