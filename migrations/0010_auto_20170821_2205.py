# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrblog', '0009_auto_20170821_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrblogpagegalleryimage',
            name='caption',
            field=models.TextField(verbose_name='Text'),
        ),
    ]
