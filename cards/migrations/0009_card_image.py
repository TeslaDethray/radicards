# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20141113_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(default='', upload_to=b'media/cards'),
            preserve_default=False,
        ),
    ]
