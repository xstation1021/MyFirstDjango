# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('prep_time', models.CharField(max_length=50, null=True, blank=True)),
                ('cook_time', models.CharField(max_length=50, null=True, blank=True)),
                ('serving_size', models.CharField(max_length=50, null=True, blank=True)),
                ('instructions', models.TextField(null=True, blank=True)),
                ('code', models.CharField(max_length=50, null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recipes',
                'managed': False,
            },
        ),
    ]
