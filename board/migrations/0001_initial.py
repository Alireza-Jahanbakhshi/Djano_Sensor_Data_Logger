# Generated by Django 4.1.3 on 2022-12-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_R', models.IntegerField(verbose_name='R of RGB')),
                ('color_G', models.IntegerField(verbose_name='G of RGB')),
                ('color_B', models.IntegerField(verbose_name='B of RGB')),
                ('date_time', models.CharField(max_length=15, verbose_name='date_time')),
                ('temp', models.IntegerField(verbose_name='temp')),
                ('humidity', models.IntegerField(verbose_name='humidity')),
                ('LED_1', models.IntegerField(verbose_name='LED1')),
                ('LED_2', models.IntegerField(verbose_name='LED2')),
                ('LED_3', models.IntegerField(verbose_name='LED3')),
                ('speaker', models.IntegerField(verbose_name='speaker')),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
        ),
    ]
