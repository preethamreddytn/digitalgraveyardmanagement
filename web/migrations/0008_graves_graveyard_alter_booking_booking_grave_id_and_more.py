# Generated by Django 5.2.1 on 2025-06-03 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_graveyardinfo_graveyard1'),
    ]

    operations = [
        migrations.CreateModel(
            name='graves',
            fields=[
                ('grave_id', models.AutoField(primary_key=True, serialize=False)),
                ('grave_no', models.IntegerField()),
                ('status', models.CharField(choices=[('buried', 'buried'), ('reserved', 'reserved'), ('available', 'available')], max_length=10)),
                ('grave_column', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='graveyard',
            fields=[
                ('graveyard_id', models.AutoField(primary_key=True, serialize=False)),
                ('graveyard_name', models.CharField(max_length=30)),
                ('graveyard_add', models.CharField(max_length=50)),
                ('graveyard_city', models.CharField(max_length=15)),
                ('graveyard_plots', models.IntegerField()),
                ('graveyard_phoneno', models.IntegerField()),
                ('graveyard_column', models.IntegerField()),
                ('graveyard_row', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_grave_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.graves'),
        ),
        migrations.AlterField(
            model_name='deceased',
            name='grave_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.graves'),
        ),
        migrations.AlterField(
            model_name='maintain',
            name='main_grave_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.graves'),
        ),
        migrations.AddField(
            model_name='graves',
            name='graveyard_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.graveyard'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='graveyard_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.graveyard'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_work_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.graveyard'),
        ),
        migrations.DeleteModel(
            name='gravesplots',
        ),
        migrations.DeleteModel(
            name='graveyard1',
        ),
    ]
