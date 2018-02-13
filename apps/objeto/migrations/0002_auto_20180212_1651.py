# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-12 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objeto', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='Facultad',
        ),
        migrations.AlterField(
            model_name='objetoa',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='objetoa',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tema',
            name='Nombre_tema',
            field=models.CharField(max_length=30),
        ),
    ]