# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-15 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default=b'', max_length=7)),
                ('municipio', models.CharField(default=b'', max_length=100)),
            ],
        ),
    ]