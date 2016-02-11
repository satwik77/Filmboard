# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_projectrequirements_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='allied',
            name='past_experiences',
            field=models.ManyToManyField(to='registration.PastExperiences', blank=True),
        ),
        migrations.AddField(
            model_name='allied',
            name='recommendations',
            field=models.ManyToManyField(to='registration.Recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='production',
            name='past_experiences',
            field=models.ManyToManyField(to='registration.PastExperiences', blank=True),
        ),
        migrations.AddField(
            model_name='production',
            name='recommendations',
            field=models.ManyToManyField(to='registration.Recommendations', blank=True),
        ),
    ]
