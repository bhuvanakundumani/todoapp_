# Generated by Django 2.0.7 on 2018-07-17 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapplist', '0002_auto_20180717_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.date(2018, 7, 17)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(),
        ),
    ]
