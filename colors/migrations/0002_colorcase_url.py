# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorcase',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
