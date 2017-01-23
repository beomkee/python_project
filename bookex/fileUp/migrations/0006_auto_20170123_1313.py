# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 04:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileUp', '0005_auto_20170118_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfilemodel',
            options={'ordering': ('-modify_date', '-pk'), 'verbose_name': 'document', 'verbose_name_plural': 'documents'},
        ),
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='user',
        ),
        migrations.AddField(
            model_name='uploadfilemodel',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
