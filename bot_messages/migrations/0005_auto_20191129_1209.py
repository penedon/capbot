# Generated by Django 2.2.7 on 2019-11-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0004_auto_20191129_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='from_bot',
            field=models.CharField(db_column='from', max_length=36),
        ),
    ]
