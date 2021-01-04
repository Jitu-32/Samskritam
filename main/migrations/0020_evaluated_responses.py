# Generated by Django 3.1.4 on 2021-01-04 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_auto_20210104_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluated_responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.competition')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]