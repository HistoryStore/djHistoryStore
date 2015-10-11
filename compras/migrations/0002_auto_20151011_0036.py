# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date_shopping',
            field=models.DateField(verbose_name=b'fecha', null=True, editable=False, blank=True),
        ),
    ]
