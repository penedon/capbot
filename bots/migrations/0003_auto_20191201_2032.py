# Generated by Django 2.2.7 on 2019-12-01 23:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_auto_20191201_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='id',
            field=models.CharField(max_length=36, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='id length has to be 36', regex='^.{36}$')]),
        ),
    ]
