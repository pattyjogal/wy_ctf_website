# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-02 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20161001_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='key_hash',
            new_name='key_hashes',
        ),
    ]
