# Generated by Django 4.2.6 on 2023-11-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_rename_sanitary_sector_restaurant_sanitary_industry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='parcel_address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='street_address',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
