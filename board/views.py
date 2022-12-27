
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
        dict_board = {}
        dict_board["color_R"]=board_data[0]
        dict_board["color_G"]=board_data[1]
        dict_board["color_B"]=board_data[2]
        dict_board["date_time"]=board_data[3]
        dict_board["temp"]=board_data[4]
        dict_board["humidity"]=board_data[5]
        dict_board["LED_1"]=board_data[6]
        dict_board["LED_2"]=board_data[7]
        dict_board["LED_3"]=board_data[8]
        dict_board["speacker"]=board_data[9]
        serializer = self.get_serializer(data=dict_board)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")


        
