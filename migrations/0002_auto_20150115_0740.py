# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigned_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bug',
            name='comments',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
