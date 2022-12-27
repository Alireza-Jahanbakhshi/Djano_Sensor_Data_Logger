
from rest_framework import serializers

from board.models import Board


class BoardSerializers(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = [
            'color_R',
            'color_G',
            'color_B',
            'date_time',
            'temp',
            'humidity',
            'LED_1',
            'LED_2',
            'LED_3',
            'speacker'
        ]
