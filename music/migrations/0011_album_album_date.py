# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 08:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_remove_album_album_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 12, 11, 8, 52, 10, 262051)),
        ),
    ]
