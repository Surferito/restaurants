# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-16 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0002_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='dishes/'),
        ),
        migrations.AddField(
            model_name='plato',
            name='precio',
            field=models.IntegerField(blank=True, default=6),
            preserve_default=False,
        ),
    ]
