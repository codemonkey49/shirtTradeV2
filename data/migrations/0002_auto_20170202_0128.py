# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-02 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='shirtImg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.shirtImage'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.teamProfile'),
        ),
    ]
