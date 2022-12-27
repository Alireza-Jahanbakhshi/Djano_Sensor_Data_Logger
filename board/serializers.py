from rest_framework import serializers

from board.models import Board


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        exclude = ["id"]

