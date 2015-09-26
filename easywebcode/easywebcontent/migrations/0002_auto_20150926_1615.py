# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easywebcontent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curated',
            name='abstract',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='curated',
            name='html',
            field=models.TextField(null=True, blank=True),
        ),
    ]
