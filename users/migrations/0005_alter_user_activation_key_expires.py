# Generated by Django 3.2.12 on 2022-03-31 14:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220327_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 14, 44, 36, 977569, tzinfo=utc)),
        ),
    ]
