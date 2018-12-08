# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-07 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0009_auto_20181207_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myurlshortner',
            name='url',
            field=models.CharField(max_length=120, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
