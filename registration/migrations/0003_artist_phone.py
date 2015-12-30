# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20151227_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
