# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-25 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='notice_type',
            field=models.CharField(default='event', max_length=50),
            preserve_default=False,
        ),
    ]
