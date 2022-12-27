from django.db import models
from datetime import datetime


class Board(models.Model):
    color_R = models.IntegerField(
        verbose_name='R of RGB'
    )
    color_G = models.IntegerField(
        verbose_name='G of RGB'
    )
    color_B = models.IntegerField(
        verbose_name='B of RGB'
    )
    date_time = models.DateTimeField(
        verbose_name='date_time'
    )
    temp = models.IntegerField(
        verbose_name='temperature'
    )
    humidity = models.IntegerField(
        verbose_name='humidity'
    )
    LED_1 = models.IntegerField(
        verbose_name='LED1'
    )
    LED_2 = models.IntegerField(
        verbose_name='LED2'
    )
    LED_3 = models.IntegerField(
        verbose_name='LED3'
    )
    speaker = models.IntegerField(
        verbose_name='speaker'
    )

    @property
    def send_data_type(self):
        """
        return wanted data types
        """
        data = [0, self.color_R, self.color_G, self.color_B, self.date_time.timestamp() * 1000, self.temp,
                self.humidity, self.LED_1, self.LED_2, self.LED_3]

        data = map(lambda x: str(x), data)

        return "/".join(data)

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return str(self.id)
