# Generated by Django 2.2.7 on 2019-11-29 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
