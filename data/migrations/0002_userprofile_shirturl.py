# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='shirtURL',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
