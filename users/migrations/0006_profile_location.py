# Generated by Django 3.1.5 on 2021-03-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(null=True, max_length=100),
        ),
    ]