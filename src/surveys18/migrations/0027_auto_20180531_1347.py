# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-31 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys18', '0026_auto_20180531_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberworkers',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Count'),
        ),
    ]
