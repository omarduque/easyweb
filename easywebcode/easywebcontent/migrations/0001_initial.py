# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=600)),
                ('category', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=400)),
                ('tool_url', models.CharField(max_length=400)),
            ],
        ),
    ]
