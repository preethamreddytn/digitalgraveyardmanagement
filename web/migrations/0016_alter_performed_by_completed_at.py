# Generated by Django 5.2.1 on 2025-06-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_maintain_main_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performed_by',
            name='completed_at',
            field=models.DurationField(),
        ),
    ]
