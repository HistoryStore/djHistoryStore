# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20151010_1702'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadenas', '0002_auto_20151010_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_shopping', models.DateField(verbose_name=b'fecha', auto_created=True)),
                ('status', models.BooleanField(default=False, verbose_name=b'status')),
                ('place', models.ForeignKey(related_query_name=b'place', related_name='places', verbose_name=b'lugar', to='cadenas.Place')),
                ('user', models.ForeignKey(verbose_name=b'usuario', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(related_query_name=b'vendor', related_name='vendors', verbose_name=b'cadena', to='cadenas.Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_uom', models.CharField(default=b'kilogram', max_length=10, verbose_name=b'tipo uom', choices=[(b'kilogram', b'Kilogramo'), (b'liter', b'Litro'), (b'piece', b'Pieza')])),
                ('price', models.DecimalField(verbose_name=b'precio', max_digits=6, decimal_places=2)),
                ('conversion', models.DecimalField(verbose_name=b'conversion', max_digits=6, decimal_places=3)),
                ('quantity', models.IntegerField(default=1, verbose_name=b'cantidad')),
                ('list', models.ForeignKey(related_query_name=b'shopping', related_name='shoppings', verbose_name=b'lista', to='compras.List')),
                ('product', models.ForeignKey(related_query_name=b'shopping', related_name='shoppings', verbose_name=b'producto', to='productos.Product')),
            ],
        ),
    ]
