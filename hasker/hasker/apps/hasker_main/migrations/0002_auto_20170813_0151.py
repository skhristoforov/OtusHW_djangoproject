# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasker_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haskertag',
            name='question',
        ),
        migrations.AddField(
            model_name='haskerquestion',
            name='tags',
            field=models.ManyToManyField(to='hasker_main.HaskerTag'),
        ),
    ]
