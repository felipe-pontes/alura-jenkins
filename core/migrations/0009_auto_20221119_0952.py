# Generated by Django 2.1.7 on 2022-11-19 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20221119_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 19, 9, 52, 45, 58178)),
        ),
    ]
