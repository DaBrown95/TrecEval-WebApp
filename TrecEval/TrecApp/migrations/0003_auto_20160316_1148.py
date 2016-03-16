# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('TrecApp', '0002_auto_20160315_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='judgement_file',
            field=models.URLField(default=datetime.date(2016, 3, 16)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='tasl_url',
            field=models.URLField(default=datetime.date(2016, 3, 16)),
            preserve_default=False,
        ),
    ]
