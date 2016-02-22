# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20160208_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='height',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='weight',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
