# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20141109_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='display_name',
            new_name='option',
        ),
        migrations.AddField(
            model_name='settings',
            name='options',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
