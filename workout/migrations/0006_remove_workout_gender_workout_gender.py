# Generated by Django 4.2.1 on 2023-05-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gender', '0001_initial'),
        ('workout', '0005_remove_workout_difficulty_workout_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='gender',
        ),
        migrations.AddField(
            model_name='workout',
            name='gender',
            field=models.ManyToManyField(to='gender.gender'),
        ),
    ]