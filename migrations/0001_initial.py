# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-11 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
    ]

    operations = [
        migrations.CreateModel(
            name='VrblogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
