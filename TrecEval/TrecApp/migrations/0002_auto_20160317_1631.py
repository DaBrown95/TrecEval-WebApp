# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TrecApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='map',
            new_name='MAP',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='run',
            name='task',
        ),
        migrations.RemoveField(
            model_name='task',
            name='track',
        ),
        migrations.AddField(
            model_name='researcher',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='user',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='run',
            name='runfile',
            field=models.FileField(default='', upload_to=b'runFiles'),
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
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='researcher',
            name='url',
            field=models.URLField(max_length=20),
        ),
    ]
