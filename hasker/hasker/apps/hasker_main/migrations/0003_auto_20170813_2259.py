# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hasker_main', '0002_auto_20170813_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='haskeranswer',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='haskerquestion',
            old_name='_id',
            new_name='id',
        ),
    ]
