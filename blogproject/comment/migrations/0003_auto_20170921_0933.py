# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-21 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20170919_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time', 'name']},
        ),
    ]
