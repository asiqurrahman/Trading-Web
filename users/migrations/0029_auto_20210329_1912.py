# Generated by Django 3.1.5 on 2021-03-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20210329_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=None, max_length=5),
        ),
    ]
