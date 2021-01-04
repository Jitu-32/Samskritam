# Generated by Django 3.1.4 on 2021-01-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_evaluated_responses'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempted_contests',
            name='evaluated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attempted_contests',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Evaluated_responses',
        ),
    ]