# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20160121_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allied',
            name='category',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allied',
            name='location',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allied',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='allied',
            name='services',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='body_type',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='email_id',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='artist',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='location',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='past_experiences',
            field=models.ManyToManyField(to='registration.PastExperiences', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='phone',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='skills',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='weight',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='location',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
