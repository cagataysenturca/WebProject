# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_album_album_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_date',
        ),
    ]
