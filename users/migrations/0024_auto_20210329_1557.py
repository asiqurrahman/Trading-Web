# Generated by Django 3.1.5 on 2021-03-29 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20210328_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=5, default=None, validators=[django.core.validators.RegexValidator('^\\d{1,9}$')]),
        ),
    ]
