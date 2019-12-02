# Generated by Django 2.2.7 on 2019-12-01 23:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0005_auto_20191129_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversationId',
            field=models.CharField(max_length=36, validators=[django.core.validators.RegexValidator(code='nomatch', message='id length has to be 36', regex='^.{36}$')]),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_bot',
            field=models.CharField(db_column='from', max_length=36, validators=[django.core.validators.RegexValidator(code='nomatch', message='from length has to be 36', regex='^.{36}$')]),
        ),
        migrations.AlterField(
            model_name='message',
            name='to',
            field=models.CharField(max_length=36, validators=[django.core.validators.RegexValidator(code='nomatch', message='to length has to be 36', regex='^.{36}$')]),
        ),
    ]