# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-12 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20180206_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreD', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreF', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='registrousuario',
            name='tipo',
            field=models.CharField(choices=[('e', 'estudiante'), ('p', 'profesor')], default=2, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrousuario',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Departamento'),
        ),
        migrations.AlterField(
            model_name='registrousuario',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Facultad'),
        ),
    ]
