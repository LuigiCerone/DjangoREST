# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0004_auto_20170616_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='userId',
        ),
    ]
