# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import paintstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=89)),
                ('image', models.ImageField(upload_to=b'/Users/tesladethray/Work/radicards/media/art')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'art',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('biography', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'/Users/tesladethray/Work/radicards/media/artist', blank=True)),
                ('url', models.CharField(max_length=144, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=55)),
                ('hashed_id', models.SlugField(max_length=55, null=True)),
                ('short_url', models.CharField(max_length=55, null=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=34)),
                ('font_file', models.FileField(null=True, upload_to=b'/Users/tesladethray/Work/radicards/media/fonts', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=55, blank=True)),
                ('last_name', models.CharField(max_length=55, blank=True)),
                ('email', models.CharField(max_length=89, blank=True)),
                ('postal_code', models.CharField(max_length=13, blank=True)),
                ('mailing_list', models.BooleanField(default=False)),
                ('referrer', models.CharField(max_length=55, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('x_coord', models.IntegerField(default=0)),
                ('y_coord', models.IntegerField(default=0)),
                ('max_width', models.IntegerField(default=0)),
                ('max_height', models.IntegerField(default=0)),
                ('text_color', paintstore.fields.ColorPickerField(max_length=7)),
                ('font_size', models.CharField(max_length=8)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('art', models.ForeignKey(to='cards.Art')),
                ('font', models.ForeignKey(to='cards.Font')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='recipient',
            field=models.ForeignKey(related_name='+', to='cards.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='sender',
            field=models.ForeignKey(related_name='+', to='cards.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='template',
            field=models.ForeignKey(to='cards.Template', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(blank=True, to='cards.Artist', null=True),
            preserve_default=True,
        ),
    ]
