# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0015_auto_20161130_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='details',
            new_name='description',
        ),
    ]