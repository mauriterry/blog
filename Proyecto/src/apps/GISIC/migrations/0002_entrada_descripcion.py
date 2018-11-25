# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('GISIC', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='descripcion',
            field=models.CharField(default=datetime.date(2018, 11, 21), max_length=200),
            preserve_default=False,
        ),
    ]
