# Generated by Django 3.1.5 on 2021-03-15 02:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210314_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Jersey City, New Jersey'),
        ),
    ]
