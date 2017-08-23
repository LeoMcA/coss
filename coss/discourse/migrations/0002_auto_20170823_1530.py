# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discoursecategory',
            old_name='category_id',
            new_name='_category_id',
        ),
        migrations.RenameField(
            model_name='discoursecategory',
            old_name='name',
            new_name='_name',
        ),
        migrations.AddField(
            model_name='discoursecategory',
            name='_api_last_queried',
            field=models.DateTimeField(null=True),
        ),
    ]
