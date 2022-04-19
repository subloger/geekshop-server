# Generated by Django 3.2.12 on 2022-04-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcategory_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='discount',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='скидка'),
        ),
    ]
