# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-20 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrblog', '0007_auto_20170812_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrblogpage',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]