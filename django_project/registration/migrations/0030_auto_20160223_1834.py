# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0029_auto_20160223_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendations',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recommendations',
            name='reco_from',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recommendations',
            name='reco_from_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
