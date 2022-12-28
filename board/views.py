from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status

from board.models import Board
from board.serializers import BoardSerializers
from board.utils import create_data_format, rgb_to_hex


class BoardAPIViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializers
    permission_classes = (AllowAny,)

    def create(self, request):
        data = request.data
        board_data = data['data'].split("/")
        board_data.pop(0)
        obj = Board.objects.all().first()
        if obj:
            serializer = self.get_serializer(obj, data=create_data_format(board_data))
        else:
            serializer = self.get_serializer(data=create_data_format(board_data))

        if not serializer.is_valid():
            return Response({
                "error": serializer.errors
            }, status=400)

        serializer.save()
        return Response({
            "data": serializer.data
        }, status=200)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.queryparams)
        if not serializer.is_valid():
            return Response({
                "error": serializer.errors
            }, status=400)

        serializer.save()
        return Response({
            "data": serializer.data
        }, status=200)

    def list(self, request):
        obj = Board.objects.all().first()
        print(obj)
        return Response({
            "data": obj.send_data_type
        }, status=200)
    


def board_view(request):
    obj = Board.objects.all().first()
    rgb = rgb_to_hex(
        obj.color_R,
        obj.color_G,
        obj.color_R
        )
    context = {"obj": obj, "rgb": rgb}
    return render(request, 'index.html', context)

