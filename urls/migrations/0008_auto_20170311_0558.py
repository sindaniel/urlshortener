# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0007_auto_20170311_0443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='urlanalitys',
            name='os',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]