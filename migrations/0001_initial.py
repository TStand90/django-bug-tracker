# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('priority', models.CharField(max_length=1, choices=[('1', 'Very Low'), ('2', 'Low'), ('3', 'Medium'), ('4', 'High'), ('5', 'Very High')])),
                ('status', models.CharField(max_length=1, choices=[('1', 'Open'), ('2', 'Closed')])),
                ('comments', models.TextField()),
                ('assigned_to', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
