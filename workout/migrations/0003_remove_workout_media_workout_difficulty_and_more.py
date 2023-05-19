# Generated by Django 4.2.1 on 2023-05-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_workout_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='media',
        ),
        migrations.AddField(
            model_name='workout',
            name='difficulty',
            field=models.CharField(default=False, max_length=255, verbose_name='Сложность'),
        ),
        migrations.AddField(
            model_name='workout',
            name='image',
            field=models.ImageField(default=False, upload_to='workouts/images', verbose_name='Обложка'),
        ),
        migrations.AddField(
            model_name='workout',
            name='inventory',
            field=models.CharField(default=False, max_length=255, verbose_name='Инвентарь'),
        ),
        migrations.AddField(
            model_name='workout',
            name='time',
            field=models.IntegerField(default=False, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.CharField(default=False, max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='gender',
            field=models.CharField(default=False, max_length=255, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='type',
            field=models.CharField(default=False, max_length=255, verbose_name='Тип'),
        ),
    ]