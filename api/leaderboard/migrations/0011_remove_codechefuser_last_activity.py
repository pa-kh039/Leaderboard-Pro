# Generated by Django 3.2.4 on 2022-08-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0010_remove_codechefuser_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codechefuser',
            name='last_activity',
        ),
    ]
