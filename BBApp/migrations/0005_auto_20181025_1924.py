# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-25 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BBApp', '0004_auto_20181025_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='estado_civil',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='cerveza_preferida',
            new_name='localidad',
        ),
    ]
