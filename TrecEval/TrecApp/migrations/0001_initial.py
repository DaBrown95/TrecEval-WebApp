# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('url', models.URLField()),
                ('display_name', models.CharField(max_length=128)),
                ('organization', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('run_type', models.IntegerField(default=0)),
                ('query_type', models.IntegerField(default=0)),
                ('feedback_type', models.IntegerField(default=0)),
                ('map', models.DecimalField(max_digits=100, decimal_places=5)),
                ('p10', models.DecimalField(max_digits=100, decimal_places=5)),
                ('p20', models.DecimalField(max_digits=100, decimal_places=5)),
                ('researcher', models.ForeignKey(to='TrecApp.Researcher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('year', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('track_url', models.URLField()),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='track',
            field=models.ForeignKey(to='TrecApp.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='run',
            name='task',
            field=models.ForeignKey(to='TrecApp.Task'),
            preserve_default=True,
        ),
    ]
