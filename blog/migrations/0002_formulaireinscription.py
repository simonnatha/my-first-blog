# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='formulaireinscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=50)),
                ('mdp', models.CharField(max_length=30)),
                ('cmdp', models.CharField(max_length=30)),
            ],
        ),
    ]