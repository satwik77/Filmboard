# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0033_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='allied',
            name='my_story',
            field=models.TextField(default=b' '),
        ),
        migrations.AlterField(
            model_name='locations',
            name='allied',
            field=models.ForeignKey(default=None, blank=True, to='registration.Allied', null=True),
        ),
    ]
