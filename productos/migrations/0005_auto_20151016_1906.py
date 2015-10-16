# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20151016_1906'),
        ('productos', '0004_auto_20151016_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='list',
            field=models.ForeignKey(related_query_name=b'product', related_name='products', verbose_name=b'lista', blank=True, to='compras.List', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, verbose_name=b'precio', max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name=b'cantidad'),
        ),
    ]
