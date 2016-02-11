# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='allied',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('sub_category', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=150)),
                ('services', models.CharField(max_length=300)),
                ('certifications', models.TextField()),
                ('phone', models.IntegerField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=150)),
                ('aboutus', models.TextField()),
                ('phone', models.IntegerField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.AlterField(
            model_name='artist',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
