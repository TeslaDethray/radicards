# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_artist_hometown'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
