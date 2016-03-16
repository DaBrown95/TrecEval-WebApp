# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrecApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='run',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(default=22),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
