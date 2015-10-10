# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadenas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'vendor')),
                ('image', models.ImageField(upload_to=b'vendor/', verbose_name=b'logo')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.CharField(max_length=b'50', null=True, verbose_name=b'latitude', blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.CharField(max_length=b'50', null=True, verbose_name=b'longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to=b'places/', verbose_name=b'logo'),
        ),
    ]
