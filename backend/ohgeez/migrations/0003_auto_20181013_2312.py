# Generated by Django 2.1.2 on 2018-10-13 23:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ohgeez', '0002_auto_20181013_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created',
        ),
        migrations.RemoveField(
            model_name='item',
            name='updated',
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
