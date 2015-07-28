# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('code', models.CharField(max_length=200, verbose_name=b'Code')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField(verbose_name=b'Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_number', models.CharField(max_length=200, verbose_name=b'Call Number')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.FloatField(verbose_name=b'Distance')),
                ('duration', models.FloatField(verbose_name=b'Duration')),
                ('arrive', models.ForeignKey(related_name='trip_arrive', to='log.Airport')),
                ('depart', models.ForeignKey(related_name='trip_depart', to='log.Airport')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='plane',
            field=models.ForeignKey(to='log.Plane'),
        ),
        migrations.AddField(
            model_name='entry',
            name='trip',
            field=models.ForeignKey(to='log.Trip'),
        ),
    ]
