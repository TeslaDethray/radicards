# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20141112_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='published',
        ),
    ]
