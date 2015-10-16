# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20151011_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='conversion',
            field=models.DecimalField(default=0, verbose_name=b'conversion', max_digits=6, decimal_places=3),
        ),
        migrations.AddField(
            model_name='product',
            name='type_uom',
            field=models.CharField(default=b'kilogram', max_length=10, verbose_name=b'tipo uom', choices=[(b'kilogram', b'Kilogramo'), (b'liter', b'Litro'), (b'piece', b'Pieza')]),
        ),
    ]
