# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-20 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0018_java_job_workyearavr'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='workYearMean',
            field=models.FloatField(null=True),
        ),
    ]