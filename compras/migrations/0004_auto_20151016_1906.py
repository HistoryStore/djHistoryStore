# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20151016_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping',
            name='list',
        ),
        migrations.RemoveField(
            model_name='shopping',
            name='product',
        ),
        migrations.RemoveField(
            model_name='list',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Shopping',
        ),
    ]
