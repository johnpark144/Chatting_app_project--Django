# Generated by Django 4.0.6 on 2022-08-26 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatting_app', '0002_chatting_room_chatting_chatting_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatting',
            name='chatting_room',
        ),
        migrations.DeleteModel(
            name='Chatting_room',
        ),
    ]
