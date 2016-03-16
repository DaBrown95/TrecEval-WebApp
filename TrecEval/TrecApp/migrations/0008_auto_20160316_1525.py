# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrecApp', '0007_auto_20160316_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='MAP',
            field=models.DecimalField(default=1.0, null=True, max_digits=100, decimal_places=5),
        ),
    ]
