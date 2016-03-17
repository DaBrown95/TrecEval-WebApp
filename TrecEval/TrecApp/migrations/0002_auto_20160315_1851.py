# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('TrecApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='map',
            new_name='MAP',
        ),
        migrations.AddField(
            model_name='run',
            name='runfile',
            field=models.FileField(default=datetime.date(2016, 3, 15), upload_to=b'runFiles'),
            preserve_default=False,
        ),
    ]
