# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20160817_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('FR', 'Forensics'), ('CR', 'Cryptography'), ('LX', 'Linux'), ('AL', 'Algorithms'), ('WB', 'Web'), ('RE', 'Reverse Engineering'), ('PW', 'Pwning')], max_length=2)),
            ],
        ),
    ]
