# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo', '0003_album_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='userId',
            field=models.IntegerField(default=0),
        ),
    ]