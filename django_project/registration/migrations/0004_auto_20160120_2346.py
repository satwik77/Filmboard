# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20160120_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2016, 1, 20, 23, 45, 8, 152599, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='description',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
    ]
