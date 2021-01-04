# Generated by Django 3.1.4 on 2021-01-04 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210104_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='fib_student_response',
            name='contest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.competition'),
        ),
        migrations.AddField(
            model_name='mcq_student_response',
            name='contest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.competition'),
        ),
    ]
