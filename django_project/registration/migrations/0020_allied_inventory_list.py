# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20160211_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='allied',
            name='inventory_list',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
