# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumohacks', '0003_auto_20160918_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='bob', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='bob', max_length=128),
            preserve_default=False,
        ),
    ]