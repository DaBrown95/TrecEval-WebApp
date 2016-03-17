# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrecApp', '0005_auto_20160316_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='MAP',
            field=models.DecimalField(default=0.0, max_digits=100, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='run',
            name='p10',
            field=models.DecimalField(default=0.0, max_digits=100, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='run',
            name='p20',
            field=models.DecimalField(default=0.0, max_digits=100, decimal_places=5),
        ),
    ]
