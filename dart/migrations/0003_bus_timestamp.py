# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dart', '0002_auto_20170916_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
