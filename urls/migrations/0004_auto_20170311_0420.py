# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0003_urlanalitys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlanalitys',
            old_name='user',
            new_name='url',
        ),
    ]