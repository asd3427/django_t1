# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20181128_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.Brand', verbose_name='所属品牌'),
        ),
    ]
