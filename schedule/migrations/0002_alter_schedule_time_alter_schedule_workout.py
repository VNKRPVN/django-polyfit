# Generated by Django 4.2.1 on 2023-05-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_remove_workout_inventory_remove_workout_type_and_more'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='workout',
            field=models.ManyToManyField(to='workout.workout'),
        ),
    ]