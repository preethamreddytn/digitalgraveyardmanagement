# Generated by Django 5.2.1 on 2025-06-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_graveplots_alter_booking_booking_grave_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graveplots',
            name='grave_column',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='graveplots',
            name='grave_row',
            field=models.IntegerField(max_length=10),
        ),
    ]
