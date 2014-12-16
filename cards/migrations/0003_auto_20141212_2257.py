# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20141212_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='extra_image',
            field=models.ImageField(null=True, upload_to=b'/home/radicaldesigns/radicards/media/templates', blank=True),
            preserve_default=True,
        ),
    ]
