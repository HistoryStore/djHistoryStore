# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'categoria')),
                ('image', models.ImageField(upload_to=b'categorias/', verbose_name=b'imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barcorde', models.CharField(max_length=140, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'nombre')),
                ('category', models.ForeignKey(verbose_name=b'categoria', to='productos.Category')),
            ],
        ),
    ]
