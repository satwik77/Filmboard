# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20160122_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='past_experiences',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='recommendations',
        ),
        migrations.DeleteModel(
            name='PastExperiences',
        ),
        migrations.DeleteModel(
            name='Recommendations',
        ),
    ]
