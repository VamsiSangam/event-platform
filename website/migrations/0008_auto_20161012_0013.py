# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_answers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='hint2',
            new_name='imagelink',
        ),
    ]
