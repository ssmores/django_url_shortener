# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default=15, max_length=15),
            preserve_default=False,
        ),
    ]
