# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-25 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170925_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateField(),
        ),
    ]
