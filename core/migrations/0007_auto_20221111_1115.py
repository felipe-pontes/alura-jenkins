# Generated by Django 2.1.7 on 2022-11-11 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20221111_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 11, 11, 15, 34, 872986)),
        ),
    ]
