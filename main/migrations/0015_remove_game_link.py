# Generated by Django 3.1.2 on 2021-01-01 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_game_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='link',
        ),
    ]
