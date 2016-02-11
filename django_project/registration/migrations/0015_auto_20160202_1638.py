# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_artist_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allied',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='phone',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
