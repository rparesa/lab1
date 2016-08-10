# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0003_auto_20160804_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='datetime',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='uri',
            field=models.URLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='statusCode',
            field=models.CharField(default='200', max_length=3),
        ),
    ]
