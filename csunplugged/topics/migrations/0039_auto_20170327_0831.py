# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0038_auto_20170327_0813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculumarea',
            old_name='children',
            new_name='parent',
        ),
    ]
