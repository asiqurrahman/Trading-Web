# Generated by Django 3.1.5 on 2021-03-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20210330_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=None, max_length=5),
        ),
    ]