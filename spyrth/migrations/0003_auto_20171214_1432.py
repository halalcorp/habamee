# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-14 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spyrth', '0002_auto_20170717_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]