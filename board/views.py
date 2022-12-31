from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from board.models import Board
from board.serializers import BoardSerializers
from board.utils import create_data_format, rgb_to_hex, hex_to_rgb


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

        new_obj = serializer.save()
        new_obj.hex_color = None
        new_obj.save()
        return Response({
            "data": serializer.data
        }, status=200)

    @action(detail=False,methods=["get"],permission_classes=[AllowAny])
    def update_board(self, request, *args, **kwargs):
        instance = Board.objects.all().first()
        params = request.query_params
        led_1 = params.get("led_1","")
        led_2 = params.get("led_2","")
        led_3 = params.get("led_3","")
        led = params.get("led","")
        print(led,'sss')
        if led_1:
            if instance.LED_1 :
                instance.LED_1 = 0
            else :
                instance.LED_1 = 1

        if led_2:
            if instance.LED_2 :
                instance.LED_2 = 0
            else :
                instance.LED_2 = 1
        
        if led_3:
            if instance.LED_3 :
                instance.LED_3 = 0
            else :
                instance.LED_3 = 1
        
        if led:
            print(led)
            instance.hex_color = led
            led = hex_to_rgb(led)
            instance.color_R = led[0]
            instance.color_G = led[1]
            instance.color_B = led[2]
        instance.save()
        return Response({
            "data" : "success"
        },status=200)



    def list(self, request):
        obj = Board.objects.all().first()
        return Response({
            "data": obj.send_data_type
        }, status=200)
    

@action(detail=False,methods=["post"],permission_classes=[IsAuthenticated])
def board_view(request):
    obj = Board.objects.all().first()
    if not obj.hex_color : 
        rgb = rgb_to_hex(
            obj.color_R,
            obj.color_G,
            obj.color_R
            )
    else :
        rgb = obj.hex_color
    context = {"obj": obj, "rgb": rgb}
    return render(request, 'index.html', context)
