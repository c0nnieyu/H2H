# Generated by Django 2.1.2 on 2018-10-13 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ohgeez', '0002_auto_20181013_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geez',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='geez',
            name='longitude',
        ),
    ]
