# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-17 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spyrth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programs',
            old_name='description',
            new_name='shortDesc',
        ),
        migrations.AlterField(
            model_name='programs',
            name='url',
            field=models.URLField(),
        ),
    ]
