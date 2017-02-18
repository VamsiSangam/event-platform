# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionid', models.AutoField(primary_key=True, serialize=False)),
                ('questiontext', models.CharField(max_length=120)),
                ('answertext', models.CharField(max_length=100)),
            ],
        ),
    ]
