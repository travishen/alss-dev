# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-31 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys18', '0024_auto_20180531_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsidy',
            name='no',
        ),
        migrations.RemoveField(
            model_name='subsidy',
            name='yes',
        ),
        migrations.AddField(
            model_name='subsidy',
            name='is_subsidy',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Is Subsidy'),
        ),
    ]
