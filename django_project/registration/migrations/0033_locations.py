# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_pastexperiences_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('allied', models.ForeignKey(default=None, blank=True, to='registration.Allied', null=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
