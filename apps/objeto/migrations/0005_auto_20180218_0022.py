# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-18 05:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objeto', '0004_auto_20180217_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetoa',
            name='sube',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
