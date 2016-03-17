# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('TrecApp', '0002_auto_20160317_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher',
            name='id',
        ),
        migrations.AlterField(
            model_name='researcher',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
