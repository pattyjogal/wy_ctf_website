# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160817_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='algo_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='crypto_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='forensic_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='linux_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pwn_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rev_eng_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='web_score',
        ),
    ]