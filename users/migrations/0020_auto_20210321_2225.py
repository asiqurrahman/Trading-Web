# Generated by Django 3.1.5 on 2021-03-22 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210321_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='placeholder', max_length=100),
        ),
    ]
