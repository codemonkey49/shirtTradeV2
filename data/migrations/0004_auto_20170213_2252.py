# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-13 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170204_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shirtImg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.shirtImage'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.teamProfile'),
        ),
    ]