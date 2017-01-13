# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='title')),
                ('docfile', models.FileField(upload_to='doucuments')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='DESCRIPTION')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
            ],
        ),
    ]