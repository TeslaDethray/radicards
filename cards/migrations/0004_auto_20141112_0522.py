# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20141112_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='font',
            name='external_url',
            field=models.CharField(max_length=144, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='font',
            name='font_file',
            field=models.FileField(null=True, upload_to=b'media/fonts', blank=True),
            preserve_default=True,
        ),
    ]
