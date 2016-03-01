# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0028_auto_20160223_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allied',
            name='recommendations',
        ),
        migrations.RemoveField(
            model_name='production',
            name='recommendations',
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='duration_end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='duration_start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='project_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='project_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='project_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='remarks',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recommendations',
            name='skills',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
