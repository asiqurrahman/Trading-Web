# Generated by Django 3.1.5 on 2021-03-29 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210321_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Enter Zipcode', max_length=5, validators=[django.core.validators.RegexValidator('^\\d{1,9}$')]),
        ),
    ]