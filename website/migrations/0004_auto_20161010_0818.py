# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20161010_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='timeanswered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
