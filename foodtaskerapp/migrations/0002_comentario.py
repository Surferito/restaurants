# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=140)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Restaurante')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Usuario')),
            ],
        ),
    ]
