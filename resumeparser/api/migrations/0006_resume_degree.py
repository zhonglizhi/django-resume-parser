# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170411_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='degree',
            field=models.TextField(default=''),
        ),
    ]