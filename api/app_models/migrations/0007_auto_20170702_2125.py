# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0006_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
