# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BBApp', '0006_auto_20181026_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='votaciones',
            old_name='user',
            new_name='usuario',
        ),
    ]
