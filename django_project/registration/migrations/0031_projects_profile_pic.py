# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0030_auto_20160223_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'pictures', blank=True),
        ),
    ]
