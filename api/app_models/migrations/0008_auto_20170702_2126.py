# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0007_auto_20170702_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]