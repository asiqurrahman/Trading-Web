# Generated by Django 3.1.5 on 2021-03-14 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content2',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
        ),
    ]
