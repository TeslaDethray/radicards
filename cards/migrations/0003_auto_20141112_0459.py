# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_template_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=34)),
                ('font_file', models.FileField(upload_to=b'media/fonts', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='template',
            name='font_file',
        ),
        migrations.AddField(
            model_name='template',
            name='font',
            field=models.ForeignKey(default='', to='cards.Font'),
            preserve_default=False,
        ),
    ]
