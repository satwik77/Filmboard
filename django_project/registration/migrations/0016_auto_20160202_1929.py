# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20160202_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'pictures', blank=True),
        ),
    ]
