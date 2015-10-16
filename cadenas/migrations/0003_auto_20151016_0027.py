# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadenas', '0002_auto_20151010_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='image',
        ),
        migrations.AddField(
            model_name='place',
            name='vendor',
            field=models.ForeignKey(related_query_name=b'vendor', verbose_name=b'vendor', blank=True, to='cadenas.Vendor', null=True),
        ),
    ]
