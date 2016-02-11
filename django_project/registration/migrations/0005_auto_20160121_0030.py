# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20160120_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectrequirements',
            old_name='skill',
            new_name='skills',
        ),
        migrations.AddField(
            model_name='projectrequirements',
            name='req_type',
            field=models.CharField(default='Artist', max_length=20, choices=[(b'Artist', b'Artist'), (b'Allied Service', b'Allied Service'), (b'Producers', b'Producers')]),
            preserve_default=False,
        ),
    ]
