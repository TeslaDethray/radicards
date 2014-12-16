# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20141212_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='hometown',
            field=models.CharField(max_length=144, null=True, blank=True),
            preserve_default=True,
        ),
    ]
