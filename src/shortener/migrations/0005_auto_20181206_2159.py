# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-06 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_myurlshortner_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myurlshortner',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]