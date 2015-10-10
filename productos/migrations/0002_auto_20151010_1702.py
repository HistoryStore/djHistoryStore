# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name=b'creado', auto_created=True)),
                ('comment', models.TextField(verbose_name=b'comentario')),
                ('qualification', models.IntegerField(default=0, verbose_name=b'calificacion')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='barcorde',
            new_name='key',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=b'categories/', verbose_name=b'imagen'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(related_query_name=b'product', related_name='products', to='productos.Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_query_name=b'comment', related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
