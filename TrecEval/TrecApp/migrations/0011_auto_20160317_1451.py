# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TrecApp', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='task',
            name='judgement_file',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tasl_url',
        ),
        migrations.AddField(
            model_name='researcher',
            name='user',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='MAP',
            field=models.DecimalField(max_digits=100, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='run',
            name='p10',
            field=models.DecimalField(max_digits=100, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='run',
            name='p20',
            field=models.DecimalField(max_digits=100, decimal_places=5),
        ),
    ]
