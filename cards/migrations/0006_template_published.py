# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_remove_template_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
