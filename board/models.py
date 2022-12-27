from django.db import models


class Board(models.Model):
    color_R = models.IntegerField(verbose_name='R of RGB')
    color_G = models.IntegerField(verbose_name='G of RGB')
    color_B = models.IntegerField(verbose_name='B of RGB')
    date_time = models.CharField(max_length=15, verbose_name='date_time')
    temp = models.IntegerField(verbose_name='temp')
    humidity = models.IntegerField(verbose_name='humidity')
    LED_1 = models.IntegerField(verbose_name='LED1')
    LED_2 = models.IntegerField(verbose_name='LED2')
    LED_3 = models.IntegerField(verbose_name='LED3')
    speacker = models.IntegerField(verbose_name='speacker')


    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.id
