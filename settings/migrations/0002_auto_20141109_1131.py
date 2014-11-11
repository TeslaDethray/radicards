# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'settings'},
        ),
        migrations.AddField(
            model_name='settings',
            name='display_name',
            field=models.CharField(max_length=144, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='help_text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
