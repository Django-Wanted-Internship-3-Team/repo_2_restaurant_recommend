# Generated by Django 4.2.6 on 2023-11-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurantlocation_alter_restaurant_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
