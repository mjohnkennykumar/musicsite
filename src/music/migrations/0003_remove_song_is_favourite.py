# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favourite',
        ),
    ]
