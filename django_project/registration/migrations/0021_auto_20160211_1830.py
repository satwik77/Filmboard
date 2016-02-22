# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_allied_inventory_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allied',
            name='inventory_list',
            field=models.CharField(default=b'', max_length=500, null=True, blank=True),
        ),
    ]
