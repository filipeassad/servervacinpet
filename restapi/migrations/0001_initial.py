# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('imagem', models.ImageField(upload_to='')),
                ('dono', models.IntegerField()),
            ],
        ),
    ]
