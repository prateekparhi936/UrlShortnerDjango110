# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-06 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_remove_myurlshortner_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='myurlshortner',
            name='shortcode',
            field=models.CharField(default='cfe', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
