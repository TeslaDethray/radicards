# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20141109_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
