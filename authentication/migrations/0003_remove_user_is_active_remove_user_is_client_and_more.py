# Generated by Django 4.2.1 on 2023-05-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=255, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=False, upload_to='user_image', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=255, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.CharField(max_length=255, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preparation',
            field=models.FloatField(default=1.0, verbose_name='Подготовка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.CharField(max_length=255, verbose_name='Вес'),
        ),
    ]
