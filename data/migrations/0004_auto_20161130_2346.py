# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 23:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20161117_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirtholdings',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]