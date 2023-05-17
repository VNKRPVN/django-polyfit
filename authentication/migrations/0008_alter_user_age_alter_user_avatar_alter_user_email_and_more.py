# Generated by Django 4.2.1 on 2023-05-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='sretgerg', null=True, upload_to='user_image', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preparation',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='Подготовка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вес'),
        ),
    ]
