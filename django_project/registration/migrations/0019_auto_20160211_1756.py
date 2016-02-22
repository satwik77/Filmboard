# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20160208_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='allied',
            name='ob_type',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='ob_type',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
