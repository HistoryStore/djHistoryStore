# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20151011_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping',
            name='conversion',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='type_uom',
        ),
    ]
